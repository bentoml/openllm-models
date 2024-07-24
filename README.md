<div align="center">
    <h1 align="center">The default model repository of <a href="https://github.com/bentoml/openllm">openllm</a></h1>
</div>

This repo (on `main` branch) is already included by openllm by default.

If you want more up-to-date untested models, please add our nightly branch.

```bash
openllm repo add nightly https://github.com/bentoml/openllm-models@nightly
```

## Supported Models

### Table of Contents

- [Llama-3.1](#llama3.1)
- [Llama-3](#llama3)
- [Phi-3](#phi3)
- [Mistral](#mistral)
- [Qwen-2](#qwen2)
- [Gemma](#gemma)
- [Llama-2](#llama2)
- [Mixtral](#mixtral)

---


### Llama-3.1 <a id="llama3.1"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama3.1 | 405b-instruct-awq-4bit-a733 | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-405B-Instruct-AWQ-INT4) |
| llama3.1 | 70b-instruct-awq-4bit-f55b | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4) |
| llama3.1 | 70b-instruct-fp16-b665 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) |
| llama3.1 | 8b-instruct-awq-4bit-f737 | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4) |
| llama3.1 | 8b-instruct-fp16-6d7b | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) |

---


### Llama-3 <a id="llama3"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama3 | 70b-instruct-awq-4bit-9204 | [HF Link](https://huggingface.co/casperhansen/llama-3-70b-instruct-awq) |
| llama3 | 70b-instruct-fp16-53f1 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) |
| llama3 | 8b-instruct-awq-4bit-985b | [HF Link](https://huggingface.co/casperhansen/llama-3-8b-instruct-awq) |
| llama3 | 8b-instruct-fp16-8638 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) |

---


### Phi-3 <a id="phi3"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| phi3 | 3.8b-instruct-fp16-c4d8 | [HF Link](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) |
| phi3 | 3.8b-instruct-ggml-q4-f5db | [HF Link](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf) |

---


### Mistral <a id="mistral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mistral | 7b-instruct-awq-4bit-332d | [HF Link](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-AWQ) |
| mistral | 7b-instruct-fp16-c489 | [HF Link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) |

---


### Qwen-2 <a id="qwen2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| qwen2 | 0.5b-instruct-fp16-0bca | [HF Link](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct) |
| qwen2 | 1.5b-instruct-fp16-f784 | [HF Link](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct) |
| qwen2 | 57b-a14b-instruct-fp16-4dcd | [HF Link](https://huggingface.co/Qwen/Qwen2-57B-A14B-Instruct) |
| qwen2 | 72b-instruct-awq-4bit-13bf | [HF Link](https://huggingface.co/Qwen/Qwen2-72B-Instruct-AWQ) |
| qwen2 | 72b-instruct-fp16-f73f | [HF Link](https://huggingface.co/Qwen/Qwen2-72B-Instruct) |
| qwen2 | 7b-instruct-awq-4bit-3150 | [HF Link](https://huggingface.co/Qwen/Qwen2-7B-Instruct-AWQ) |
| qwen2 | 7b-instruct-fp16-0016 | [HF Link](https://huggingface.co/Qwen/Qwen2-7B-Instruct) |

---


### Gemma <a id="gemma"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| gemma | 2b-instruct-fp16-f020 | [HF Link](https://huggingface.co/google/gemma-2b-it) |
| gemma | 7b-instruct-awq-4bit-2eed | [HF Link](https://huggingface.co/casperhansen/gemma-7b-it-awq) |
| gemma | 7b-instruct-fp16-1e96 | [HF Link](https://huggingface.co/google/gemma-7b-it) |

---


### Llama-2 <a id="llama2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama2 | 13b-chat-fp16-603a | [HF Link](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) |
| llama2 | 70b-chat-fp16-11af | [HF Link](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) |
| llama2 | 7b-chat-awq-4bit-c733 | [HF Link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-AWQ) |
| llama2 | 7b-chat-fp16-b8c6 | [HF Link](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) |

---


### Mixtral <a id="mixtral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mixtral | 8x7b-instruct-v0.1-awq-4bit-7682 | [HF Link](https://huggingface.co/casperhansen/mixtral-instruct-awq) |
| mixtral | 8x7b-instruct-v0.1-fp16-572d | [HF Link](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) |

---

