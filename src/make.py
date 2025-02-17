# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "bentoml",
#     "pyyaml",
#     "tomli",
#     "tomli-w",
#     "rich",
# ]
# ///
import hashlib, os, pathlib, shutil, subprocess, sys, tempfile, importlib.metadata, argparse, multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import List

import yaml, tomli_w
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


@dataclass
class BuildResult:
    model_name: str
    model_version: str
    success: bool
    error: str = ''


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


def ensure_venv(requirements_txt, venv_dir):
    if not venv_dir.exists():
        subprocess.run([sys.executable, '-m', 'uv', 'venv', venv_dir, '-p', '3.9'], check=True, capture_output=True)
        subprocess.run(
            [
                sys.executable,
                '-m',
                'uv',
                'pip',
                'install',
                '--prerelease=allow',
                'bentoml==1.4.0a2',
                '-p',
                venv_dir / 'bin' / 'python',
            ],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            [sys.executable, '-m', 'uv', 'pip', 'install', '-r', requirements_txt, '-p', venv_dir / 'bin' / 'python'],
            check=True,
            capture_output=True,
        )
    return venv_dir


def build_model(model_name: str, config: dict, progress: Progress, task_id: int) -> BuildResult:
    """Build a single model's bento."""
    try:
        with tempfile.TemporaryDirectory() as tempdir:
            progress.update(task_id, description=f'[blue]Building {model_name}...[/]')
            tempdir = pathlib.Path(tempdir)
            project = config['project']
            model_repo, model_version = model_name.split(':')
            req_txt_file = tempdir / 'requirements.txt'

            shutil.copytree(project, tempdir, dirs_exist_ok=True)

            with open(tempdir / 'openllm_config.yaml', 'w') as f:
                f.write(yaml.dump(config))

            requirements = config.get('requirements', [])
            if requirements:
                with req_txt_file.open('a') as f:
                    for req in requirements:
                        f.write(f'{req}\n')
            with (pathlib.Path(project) / 'requirements.txt').open('r') as f:
                requirements.extend(f.readlines())

            with (tempdir / 'pyproject.toml').open('rb') as s:
                data = tomllib.load(s)
                bento_yaml = data.get('tool', {}).get('bentoml', {}).get('build', {})

            with (tempdir / 'pyproject.toml').open('wb') as f:
                data['project']['version'] = importlib.metadata.version('bentoml')
                data['project']['name'] = model_repo
                data['project']['dependencies'] = requirements
                data['tool']['bentoml']['build'] = bento_yaml
                tomli_w.dump(data, f, indent=2)

            directory_hash = hash_directory(tempdir)
            model_version = f'{model_version}-{directory_hash[:4]}'

            bento_path = BENTOML_HOME / 'bentos' / model_repo / model_version

            if bento_path.exists():
                return BuildResult(model_name, model_version, True)

            # prepare venv
            venv_dir = pathlib.Path('venv').absolute() / f'{project}-{hash_file(req_txt_file)[:7]}'
            version_path = ensure_venv(req_txt_file, venv_dir)

            proc = subprocess.run(
                [
                    version_path / 'bin' / 'python',
                    '-m',
                    'bentoml',
                    'build',
                    '--version',
                    model_version,
                    '--output',
                    'tag',
                ],
                check=True,
                capture_output=True,
                cwd=tempdir,
                env=os.environ,
            )

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
                        BENTOML_HOME / 'bentos' / model_repo / model_version,
                        BENTOML_HOME / 'bentos' / model_repo / alias,
                    )

            return BuildResult(model_name, model_version, True, proc.stdout)
    except Exception as e:
        return BuildResult(model_name, '', False, str(e))


def build_all_models(recipe: dict, workers: int) -> List[BuildResult]:
    """Build all models in parallel using a thread pool."""
    console = Console()
    results = []

    with Progress(
        SpinnerColumn(), TextColumn('[progress.description]{task.description}'), console=console
    ) as progress:
        overall_task = progress.add_task('[yellow]Building bentos...[/]', total=len(recipe))
        build_tasks = {model: progress.add_task(f'[cyan]Waiting to build {model}...[/]', total=1) for model in recipe}

        with ThreadPoolExecutor(max_workers=workers) as executor:
            future_to_model = {
                executor.submit(build_model, model, cfg, progress, build_tasks[model]): model
                for model, cfg in recipe.items()
            }

            for future in as_completed(future_to_model):
                result = future.result()
                results.append(result)
                progress.advance(overall_task)
                model_task = build_tasks[result.model_name]

                if result.success:
                    progress.update(model_task, description=f'[green]✓: {result.model_version}[/]', completed=1)
                else:
                    progress.update(model_task, description=f'[red]✗: {result.error}[/]', completed=1)

    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build all model bentos in parallel')
    parser.add_argument(
        'model_names', nargs='*', help='Specific model names to build. If not provided, builds all models.'
    )
    parser.add_argument(
        '--workers',
        type=int,
        default=multiprocessing.cpu_count(),
        help=f'Number of parallel workers (default: {multiprocessing.cpu_count()})',
    )
    args = parser.parse_args()

    if args.model_names:
        invalid_models = [model for model in args.model_names if model not in RECIPE]
        if invalid_models:
            print(f'Error: Models not found in recipe.yaml: {", ".join(invalid_models)}')
            sys.exit(1)
        filtered_recipe = {model: RECIPE[model] for model in args.model_names}
    else:
        filtered_recipe = RECIPE

    print(f'Building {len(filtered_recipe)} bentos with {args.workers} workers')

    results = build_all_models(filtered_recipe, args.workers)
    successful_builds = [r for r in results if r.success]

    # Print summary
    print('\nBuild Summary:')
    print(f'Total bentos: {len(filtered_recipe)}')
    print(f'Successful builds: {len(successful_builds)}')
    print(f'Failed builds: {len(results) - len(successful_builds)}')

    if not args.model_names:
        for bento_path in BENTOML_HOME.glob('bentos/*/*'):
            if (
                bento_path.exists()
                and bento_path.is_dir()
                and not any(
                    r.model_name == bento_path.parent.name and r.model_version == bento_path.name
                    for r in successful_builds
                )
            ):
                print(f'Deleting unused bento {bento_path}')
                shutil.rmtree(bento_path)

    raise (SystemExit(0 if len(successful_builds) == len(filtered_recipe) else 1))
