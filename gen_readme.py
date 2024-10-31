from jinja2 import Environment, FileSystemLoader
import subprocess
import sys


model_list = subprocess.check_output(
    [sys.executable, "-m", "openllm", "model", "list"],
    env={"OPENLLM_TEST_REPO": "."},
)

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("readme_md.tpl")

readme_content = template.render(
    model_list=model_list.decode("utf-8"),
)

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
