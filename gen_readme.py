import os
import yaml
import glob
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader

root_dir = "bentoml/bentos"
grouped_data = defaultdict(list)

model_display_names = {
    "llama3.1": "Llama-3.1",
    "llama3": "Llama-3",
    "phi3": "Phi-3",
    "mistral": "Mistral",
    "qwen2": "Qwen-2",
    "gemma": "Gemma",
    "gemma2": "Gemma-2",
    "llama2": "Llama-2",
    "mixtral": "Mixtral",
    "mistral-large": "Mistral-Large",
    "codestral": "Codestral",
}

model_priority = {
    "llama3.1": 1,
    "llama3": 2,
    "phi3": 3,
    "mistral": 4,
    "gemma2": 5,
    "qwen2": 6,
    "gemma": 7,
    "llama2": 8,
    "mixtral": 9,
    "mistral-large": 10,
    "codestral": 11,
}

yaml_files = glob.glob(os.path.join(root_dir, "**/bento.yaml"), recursive=True)

# Read each bento.yaml file and group data by "name" field
for yaml_file in yaml_files:
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)
        # Extract the HF model ID from routes.input.model.default
        for route in data.get("schema", {}).get("routes", []):
            for prop, details in route.get("input", {}).get("properties", {}).items():
                if prop == "model" and "default" in details:
                    data["hf_model"] = details["default"]
                    break
        # Append data to grouped_data
        if "name" in data and "version" in data and "hf_model" in data:
            grouped_data[data["name"]].append(
                {
                    "name": data["name"],
                    "version": data["version"],
                    "hf_model": data["hf_model"],
                }
            )

# Deduplicate entries
for name in grouped_data:
    seen = set()
    deduped_items = []
    for item in grouped_data[name]:
        item_tuple = (item["name"], item["version"], item["hf_model"])
        if item_tuple not in seen:
            seen.add(item_tuple)
            deduped_items.append(item)
    grouped_data[name] = deduped_items

# Sort the items within each group by version
for name in grouped_data:
    grouped_data[name] = sorted(grouped_data[name], key=lambda x: x["version"])

# Sort the model names by priority and transform grouped_data into a list
sorted_grouped_data = sorted(
    grouped_data.items(), key=lambda x: model_priority.get(x[0], float("inf"))
)

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("readme_md.tpl")

readme_content = template.render(
    grouped_data=sorted_grouped_data, model_display_names=model_display_names
)

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
