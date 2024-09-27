import os
import yaml
import glob
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader

root_dir = "bentoml/bentos"
grouped_data = defaultdict(list)

model_display_names = {
    "llama3.2": "Llama-3.2",
    "llama3.1": "Llama-3.1",
    "llama3": "Llama-3",
    "llama2": "Llama-2",
    "phi3": "Phi-3",
    "mistral": "Mistral",
    "qwen2.5": "Qwen-2.5",
    "qwen2": "Qwen-2",
    "gemma2": "Gemma-2",
    "gemma": "Gemma",
    "mixtral": "Mixtral",
    "mistral-large": "Mistral-Large",
    "codestral": "Codestral",
    "pixtral": "Pixtral",
}

model_priority = {
    "llama3.2": 1,
    "llama3.1": 2,
    "phi3": 3,
    "mistral": 4,
    "gemma2": 5,
    "qwen2.5": 6,
    "mixtral": 7,
    "mistral-large": 8,
    "codestral": 9,
}

yaml_files = glob.glob(os.path.join(root_dir, "**/bento.yaml"), recursive=True)

# Read each bento.yaml file and group data by "name" field
for yaml_file in yaml_files:
    with open(yaml_file, "r") as f:
        data = yaml.safe_load(f)
        if data['name'] not in model_display_names:
            print(f"Skipping {data['name']} as it is not in model_display_names")
            continue
        # Append data to grouped_data
        if "name" in data and "version" in data and 'labels' in data and "model_name" in data['labels']:
            grouped_data[data["name"]].append(
                {
                    "name": data["name"],
                    "version": data["version"],
                    "model_name": data["labels"]["model_name"],
                }
            )
        else:
            print(f"Skipping {data['name']} as it does not have all required fields, reason: {data}")
print(grouped_data)

# Deduplicate entries
for name in grouped_data:
    seen = set()
    deduped_items = []
    for item in grouped_data[name]:
        item_tuple = (item["name"], item["version"], item["model_name"])
        if item_tuple not in seen:
            seen.add(item_tuple)
            deduped_items.append(item)
    grouped_data[name] = deduped_items

print(grouped_data)

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
    grouped_data=sorted_grouped_data,
    model_display_names=model_display_names,
)

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
