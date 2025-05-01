# OpenLLM service for neuralmagic/DeepSeek-R1-Distill-Qwen-14B-quantized.w8a8

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
  "max_model_len": 4096,
  "reasoning_parser": "deepseek_r1",
  "tensor_parallel_size": 1,
  "tool_call_parser": "llama3_json"
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
    model="neuralmagic/DeepSeek-R1-Distill-Qwen-14B-quantized.w8a8",
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
openllm deploy deepseek:r1-qwen2.5-14b-w8a8
```