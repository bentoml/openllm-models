import hashlib
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

import yaml

with open("recipe.yaml") as f:
    RECIPE = yaml.safe_load(f)


BENTOML_HOME = pathlib.Path(os.environ["BENTOML_HOME"])


def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
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


def ensure_venv(req_txt_file, venv_dir):
    if not venv_dir.exists():
        subprocess.run(
            [
                sys.executable,
                "-m",
                "uv",
                "venv",
                venv_dir,
                "-p",
                "3.9",
            ],
            check=True,
        )
        subprocess.run(
            [
                sys.executable,
                "-m",
                "uv",
                "pip",
                "install",
                "bentoml",
                "-p",
                venv_dir/"bin"/"python",
            ],
            check=True,
        )
        subprocess.run(
            [
                sys.executable,
                "-m",
                "uv",
                "pip",
                "install",
                "-r",
                req_txt_file,
                "-p",
                venv_dir/"bin"/"python",
            ],
            check=True,
        )
    return venv_dir


if __name__ == "__main__":
    if len(sys.argv) == 2:
        specified_model = sys.argv[1]
        if specified_model not in RECIPE:
            raise ValueError(f"Model {specified_model} not found in recipe")
    else:
        specified_model = None

    built_bentos = set()

    for model_name, config in RECIPE.items():
        if specified_model and model_name != specified_model:
            continue

        project = config["project"]
        model_repo, model_version = model_name.split(":")

        with tempfile.TemporaryDirectory() as tempdir:
            tempdir = pathlib.Path(tempdir)
            shutil.copytree(project, tempdir, dirs_exist_ok=True)

            with open(tempdir / "openllm_config.yaml", "w") as f:
                f.write(yaml.dump(config))

            labels = config.get("extra_labels", {})
            envs = config.get("extra_envs", [])
            yaml_content = yaml.load(
                (tempdir / "bentofile.yaml").read_text(), Loader=yaml.SafeLoader
            )
            with open(tempdir / "bentofile.yaml", "w") as f:
                yaml_content["labels"] = dict(yaml_content.get("labels", {}), **labels)
                yaml_content["envs"] = yaml_content.get("envs", []) + envs
                f.write(yaml.dump(yaml_content))

            requirements = config.get("extra_requirements", [])
            with open(tempdir / "requirements.txt", "a") as f:
                for req in requirements:
                    f.write(req + "\n")

            directory_hash = hash_directory(tempdir)
            model_version = f"{model_version}-{directory_hash[:4]}"

            bento_path = BENTOML_HOME / "bentos" / model_repo / model_version
            built_bentos.add((model_repo, model_version))

            if bento_path.exists():
                print(
                    f"Model {model_name} with version {model_version} already exists, skipping"
                )
                continue

            # prepare venv
            req_txt_file = tempdir / "requirements.txt"
            venv_dir = pathlib.Path("venv").absolute() / f"{project}-{hash_file(req_txt_file)[:7]}"
            version_path = ensure_venv(req_txt_file, venv_dir)

            subprocess.run(
                [
                    version_path / "bin" / "python",
                    "-m",
                    "bentoml",
                    "build",
                    str(tempdir),
                    "--version",
                    model_version,
                ],
                check=True,
                cwd=tempdir,
                env=os.environ,
            )

            # delete latest
            (BENTOML_HOME / "bentos" / model_repo / "latest").unlink(missing_ok=True)

            # link alias
            for alias in config.get("alias", []):
                if alias == "latest":
                    ALIAS_PATH = BENTOML_HOME / "bentos" / model_repo / alias
                    if ALIAS_PATH.exists():
                        continue
                    with open(ALIAS_PATH, "w") as f:
                        f.write(model_version)
                else:  # bentoml currently only support latest alias, copy to other alias
                    shutil.copytree(
                        BENTOML_HOME / "bentos" / model_repo / model_version,
                        BENTOML_HOME / "bentos" / model_repo / alias,
                    )

    if not specified_model:
        for bento_path in BENTOML_HOME.glob("bentos/*/*"):
            if (
                bento_path.exists()
                and bento_path.is_dir()
                and (bento_path.parent.name, bento_path.name) not in built_bentos
            ):
                print(f"Deleting unused bento {bento_path}")
                shutil.rmtree(bento_path)
