# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "bentoml",
#     "pyyaml",
#     "ruff",
#     "tomli",
#     "tomli-w",
# ]
# ///
import hashlib, os, pathlib, shutil, subprocess, sys, tempfile, importlib.metadata, yaml, tomli_w

if sys.version_info >= (3, 11):
  import tomllib
else:
  import tomli as tomllib

with open('recipe.yaml') as f:
  RECIPE = yaml.safe_load(f)


BENTOML_HOME = pathlib.Path(os.environ['BENTOML_HOME'])


def hash_file(file_path):
  hasher = hashlib.sha256()
  with open(file_path, 'rb') as f:
    for chunk in iter(lambda: f.read(4096), b''):
      hasher.update(chunk)
  return hasher.hexdigest()


def hash_directory(directory_path):
  hasher = hashlib.sha256()

  for root, _, files in sorted(os.walk(directory_path)):
    for file in sorted(files):
      file_path = os.path.join(root, file)
      file_hash = hash_file(file_path)
      hasher.update(file_hash.encode())

  return hasher.hexdigest()


if __name__ == '__main__':
  if len(sys.argv) == 2:
    specified_model = sys.argv[1]
    if specified_model not in RECIPE:
      raise ValueError(f'Model {specified_model} not found in recipe')
  else:
    specified_model = None

  built_bentos = set()

  for model_name, config in RECIPE.items():
    if specified_model and model_name != specified_model:
      continue

    project = config['project']
    model_repo, model_version = model_name.split(':')

    with tempfile.TemporaryDirectory() as tempdir:
      tempdir = pathlib.Path(tempdir)
      shutil.copytree(project, tempdir, dirs_exist_ok=True)

      with open(tempdir / 'openllm-config.yaml', 'w') as f:
        f.write(yaml.dump(config))

      labels = config.get('labels', {})
      req_txt_file = tempdir / 'requirements.txt'
      requirements = config.get('requirements', [])
      if requirements:
        with req_txt_file.open('a+') as f:
          for r in requirements:
            f.write(f'{r}\n')

      with (tempdir / 'pyproject.toml').open('rb') as s:
        data = tomllib.load(s)
        bento_yaml = data.get('tool', {}).get('bentoml', {}).get('build', {})

      with (tempdir / 'pyproject.toml').open('wb') as f:
        bento_yaml['labels'] = dict(data.get('labels', {}), **labels)
        data['project']['version'] = importlib.metadata.version('bentoml')
        data['project']['name'] = model_repo
        data['tool']['bentoml']['build'] = bento_yaml
        tomli_w.dump(data, f, indent=2)

      directory_hash = hash_directory(tempdir)
      model_version = f'{model_version}-{directory_hash[:4]}'

      bento_path = BENTOML_HOME / 'bentos' / model_repo / model_version
      built_bentos.add((model_repo, model_version))

      if bento_path.exists():
        print(f'Model {model_name} with version {model_version} already exists, skipping')
        continue

      try:
        result = subprocess.run(
          ['uv', 'pip', 'install', '-r', req_txt_file], check=True, capture_output=True, text=True
        )
        print(f'Successfully installed requirements for {model_name}')
      except subprocess.CalledProcessError as e:
        print(f'Error installing requirements for {model_name}:')
        print(f'Command: {e.cmd}')
        print(f'Return code: {e.returncode}')
        print(f'Output: {e.stdout}')
        print(f'Error: {e.stderr}')
        raise

      try:
        result = subprocess.run(
          ['bentoml', 'build', str(tempdir), '--version', model_version],
          check=True,
          capture_output=True,
          text=True,
          cwd=tempdir,
          env=os.environ,
        )
        print(f'Successfully built {model_repo}:{model_version}')
      except subprocess.CalledProcessError as e:
        print(f'Error building {model_repo}:{model_version}:')
        print(f'Command: {e.cmd}')
        print(f'Return code: {e.returncode}')
        print(f'Output: {e.stdout}')
        print(f'Error: {e.stderr}')
        raise

      # delete latest
      (BENTOML_HOME / 'bentos' / model_repo / 'latest').unlink(missing_ok=True)

      # link alias
      for alias in config.get('alias', []):
        if alias == 'latest':
          ALIAS_PATH = BENTOML_HOME / 'bentos' / model_repo / alias
          if ALIAS_PATH.exists():
            continue
          with open(ALIAS_PATH, 'w') as f:
            f.write(model_version)
        else:  # bentoml currently only support latest alias, copy to other alias
          shutil.copytree(
            BENTOML_HOME / 'bentos' / model_repo / model_version, BENTOML_HOME / 'bentos' / model_repo / alias
          )

  if not specified_model:
    for bento_path in BENTOML_HOME.glob('bentos/*/*'):
      if bento_path.exists() and bento_path.is_dir() and (bento_path.parent.name, bento_path.name) not in built_bentos:
        print(f'Deleting unused bento {bento_path}')
        shutil.rmtree(bento_path)

  # run ruff format with 4 spaces against /bentos folder
  try:
    result = subprocess.run(
      [
        'ruff',
        'format',
        '--isolated',
        '--config',
        'indent-width=4',
        '--config',
        'line-length=119',
        '--config',
        'preview=true',
        str(BENTOML_HOME / 'bentos'),
      ],
      check=True,
      capture_output=True,
      text=True,
    )
    print(f'Successfully formatted Python files in {BENTOML_HOME / "bentos"} with ruff')
  except subprocess.CalledProcessError as e:
    print(f'Error formatting Python files with ruff:')
    print(f'Command: {e.cmd}')
    print(f'Return code: {e.returncode}')
    print(f'Output: {e.stdout}')
    print(f'Error: {e.stderr}')
    raise
  print(f'Formatted Python files in {BENTOML_HOME / "bentos"} with ruff')
