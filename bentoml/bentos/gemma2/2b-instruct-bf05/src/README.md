# OpenLLM service for google/gemma-2-2b-it

- ⚡ High-performance inference using vLLM
- 💬 Streaming responses for chat completions
- 🔄 OpenAI-compatible API for easy integration
- 🎨 Chat UI for interacting with the model

## API Endpoints

- `/v1/chat/completions` - For chat completions
- `/v1/models` - To list available models

## Service Configuration

This model was configured with the following settings:

```yaml
{
  "chat_template": "{% if messages[0][\u0027role\u0027] == \u0027system\u0027 %}\n    {% set loop_messages = messages[1:] %}\n    {% set system_message = messages[0][\u0027content\u0027].strip() + \u0027\\n\\n\u0027 %}\n{% else %}\n    {% set loop_messages = messages %}\n    {% set system_message = \u0027\u0027 %}\n{% endif %}\n\n{% for message in loop_messages %}\n    {% if (message[\u0027role\u0027] == \u0027user\u0027) != (loop.index0 % 2 == 0) %}\n        {{ raise_exception(\u0027Conversation roles must alternate user/assistant/user/assistant/...\u0027) }}\n    {% endif %}\n\n    {% if loop.index0 == 0 %}\n        {% set content = system_message + message[\u0027content\u0027] %}\n    {% else %}\n        {% set content = message[\u0027content\u0027] %}\n    {% endif %}\n\n    {% if (message[\u0027role\u0027] == \u0027assistant\u0027) %}\n        {% set role = \u0027model\u0027 %}\n    {% else %}\n        {% set role = message[\u0027role\u0027] %}\n    {% endif %}\n\n    {{ \u0027\u003cstart_of_turn\u003e\u0027 + role + \u0027\\n\u0027 + content.strip() + \u0027\u003cend_of_turn\u003e\\n\u0027 }}\n\n    {% if loop.last and message[\u0027role\u0027] == \u0027user\u0027 and add_generation_prompt %}\n        {{\u0027\u003cstart_of_turn\u003emodel\\n\u0027}}\n    {% endif %}\n{% endfor %}\n",
  "dtype": "half",
  "enable_prefix_caching": false,
  "max_model_len": 3192
}
```

## Usage

To use this model, you can interact with it using the OpenAI API format. Here's a sample:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:3000/v1",
    api_key="dummy"
)

for chunk in client.chat.completions.create(
    model="google/gemma-2-2b-it",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about programming."}
    ],
    stream=True
):
  if chunk.choices[0].delta.content: print(chunk.choices[0].delta.content, end="")
```

## Deployment

```bash
openllm deploy gemma2:2b
```