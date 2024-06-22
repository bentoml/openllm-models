<div align="center">
    <h1 align="center">The default Bento model library of <a href="https://github.com/bentoml/openllm-next">openllm-next</a></h1>
</div>

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
