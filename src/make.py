# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "bentoml",
#     "pyyaml",
#     "ruff",
#     "tomli",
#     "tomli-w",
#     "jinja2",
# ]
# ///
import hashlib, os, pathlib, shutil, subprocess, sys, tempfile, importlib.metadata, yaml, tomli_w, jinja2

if sys.version_info >= (3, 11):
  import tomllib
else:
  import tomli as tomllib

with open('recipe.yaml') as f:
  RECIPE = yaml.safe_load(f)


BENTOML_HOME = pathlib.Path(os.environ['BENTOML_HOME'])
SCRIPT_DIR = pathlib.Path(__file__).parent
TEMPLATES_DIR = SCRIPT_DIR / 'templates'


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


def prepare_template_context(config, model_repo, alias):
  """Prepare a context dictionary for template rendering."""
  engine_config_struct = config.get("engine_config", {"model": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"})
  model = engine_config_struct.pop("model")
  use_mla = engine_config_struct.get("use_mla", False)
  service_config = config.get('service_config', {})

  if "envs" not in service_config:
    service_config["envs"] = []

  service_config["envs"].extend([
    {"name": "UV_NO_PROGRESS", "value": "1"},
    {"name": "HF_HUB_DISABLE_PROGRESS_BARS", "value": "1"},
    {"name": "VLLM_ATTENTION_BACKEND", "value": "FLASHMLA" if use_mla else "FLASH_ATTN"},
    {"name": "VLLM_USE_V1", "value": "1"},
  ])

  build_config = config.get('build', {})
  if 'exclude' not in build_config:
    build_config['exclude'] = []
  build_config["exclude"] = [*build_config["exclude"], "*.pth", "*.pt", "original/**/*"]

  if "post" not in build_config:
    build_config["post"] = []
  build_config["post"].append(
    "uv pip install --compile-bytecode flashinfer-python --find-links https://flashinfer.ai/whl/cu124/torch2.6"
  )

  context = {
    'model_id': model,
    'engine_config': engine_config_struct,
    'service_config': service_config,
    'build': build_config,
    'alias': config.get('alias', []),
    'exclude': build_config['exclude'],
    'vision': config.get('vision', False),
    'embeddings': config.get('embeddings', False),
    'reasoning': config.get('reasoning', False),
    'tag': f'{model_repo}:{alias}'
  }

  requirements = config.get("requirements", [])
  if len(requirements) > 0:
    context["requirements"] = requirements

  return context


def generate_files_from_templates(config, target_dir, model_repo, alias):
  env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))

  context = prepare_template_context(config, model_repo, alias)

  for template_path in TEMPLATES_DIR.glob('*.j2'):
    template_name = template_path.stem
    output_filename = template_name

    # Render template
    template = env.get_template(template_path.name)
    rendered = template.render(**context)

    # Write rendered content
    output_path = target_dir / output_filename
    with open(output_path, 'w') as f:
      f.write(rendered)


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

      # Copy project base files
      shutil.copytree(project, tempdir, dirs_exist_ok=True)

      aliases = config.get('alias', [])

      # Generate templated files
      generate_files_from_templates(config, tempdir, model_repo, aliases[0])

      labels = config.get('labels', {})

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
          ['uv', 'pip', 'install', '-r', tempdir / 'requirements.txt'], check=True, capture_output=True, text=True
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
      for alias in aliases:
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
