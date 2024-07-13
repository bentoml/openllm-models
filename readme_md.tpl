<div align="center">
    <h1 align="center">The default model repository of <a href="https://github.com/bentoml/openllm">openllm</a></h1>
</div>

This repo (on `main` branch) is already included by openllm by default.

If you want more up-to-date untested models, please add our nightly branch.

```bash
openllm repo add nightly https://github.com/bentoml/openllm@nightly
```

## Supported Models

### Table of Contents
{% for name, items in grouped_data %}
- [{{ model_display_names[name] }}](#{{ name | lower | replace(" ", "-") }})
{%- endfor %}

---

{% for name, items in grouped_data %}
### {{ model_display_names[name] }} <a id="{{ name | lower | replace(" ", "-") }}"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
{%- for item in items %}
| {{ item.name }} | {{ item.version }} | [HF Link](https://huggingface.co/{{ item.hf_model }}) |
{%- endfor %}

---

{% endfor %}
