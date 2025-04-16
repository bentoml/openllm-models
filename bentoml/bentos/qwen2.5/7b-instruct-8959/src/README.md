# OpenLLM service for Qwen/Qwen2.5-7B-Instruct

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
  "enable_auto_tool_choice": true,
  "max_model_len": 8192,
  "tool_call_parser": "hermes"
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
    model="Qwen/Qwen2.5-7B-Instruct",
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
openllm deploy qwen2.5:7b
```