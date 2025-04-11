# OpenLLM service for mistralai/Pixtral-Large-Instruct-2411

- 📸 Image-to-text capabilities for multimodal inputs
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
  "dtype": "half",
  "enable_chunked_prefill": false,
  "enable_prefix_caching": false,
  "limit_mm_per_prompt": {
    "image": 5
  },
  "max_model_len": 16384,
  "tensor_parallel_size": 4,
  "tokenizer_mode": "mistral"
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
    model="mistralai/Pixtral-Large-Instruct-2411",
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
openllm deploy pixtral:124b-2411
```