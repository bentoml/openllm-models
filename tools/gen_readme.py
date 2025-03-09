# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "jinja2",
#     "openllm",
# ]
# ///
import subprocess, pathlib, sys, jinja2

with ((GIT_ROOT:=pathlib.Path(__file__).parent.parent)/".github"/"README.md").open('w') as f: f.write(jinja2.Environment(loader=jinja2.FileSystemLoader((GIT_ROOT/"tools").__fspath__())).get_template('README.md.j2').render(model_list=subprocess.check_output([sys.executable, '-m', 'openllm', 'model', 'list'], env={'OPENLLM_TEST_REPO': '.'}).decode('utf-8')))
