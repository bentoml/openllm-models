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
- [Gemma-2](#gemma2)
- [Qwen-2](#qwen2)
- [Gemma](#gemma)
- [Llama-2](#llama2)
- [Mixtral](#mixtral)
- [Mistral-Large](#mistral-large)
- [Codestral](#codestral)

---


### Llama-3.1 <a id="llama3.1"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama3.1 | 405b-instruct-awq-4bit-df2a | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-405B-Instruct-AWQ-INT4) |
| llama3.1 | 70b-instruct-awq-4bit-2988 | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4) |
| llama3.1 | 70b-instruct-fp16-ace8 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) |
| llama3.1 | 8b-instruct-awq-4bit-fe8c | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4) |
| llama3.1 | 8b-instruct-fp16-2f36 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) |

---


### Llama-3 <a id="llama3"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama3 | 70b-instruct-awq-4bit-aebb | [HF Link](https://huggingface.co/casperhansen/llama-3-70b-instruct-awq) |
| llama3 | 70b-instruct-fp16-1315 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) |
| llama3 | 8b-instruct-awq-4bit-3f34 | [HF Link](https://huggingface.co/casperhansen/llama-3-8b-instruct-awq) |
| llama3 | 8b-instruct-fp16-8f83 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) |

---


### Phi-3 <a id="phi3"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| phi3 | 3.8b-instruct-fp16-166c | [HF Link](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) |
| phi3 | 3.8b-instruct-ggml-q4-8789 | [HF Link](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf) |

---


### Mistral <a id="mistral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mistral | 24b-instruct-nemo-ec54 | [HF Link](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) |
| mistral | 7b-instruct-awq-4bit-01cd | [HF Link](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-AWQ) |
| mistral | 7b-instruct-fp16-e1cd | [HF Link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) |

---


### Gemma-2 <a id="gemma2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| gemma2 | 27b-instruct-fp16-6b83 | [HF Link](https://huggingface.co/google/gemma-2-27b-it) |
| gemma2 | 9b-instruct-fp16-6e86 | [HF Link](https://huggingface.co/google/gemma-2-9b-it) |

---


### Qwen-2 <a id="qwen2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| qwen2 | 0.5b-instruct-fp16-33df | [HF Link](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct) |
| qwen2 | 1.5b-instruct-fp16-7cda | [HF Link](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct) |
| qwen2 | 57b-a14b-instruct-fp16-365f | [HF Link](https://huggingface.co/Qwen/Qwen2-57B-A14B-Instruct) |
| qwen2 | 72b-instruct-awq-4bit-33fa | [HF Link](https://huggingface.co/Qwen/Qwen2-72B-Instruct-AWQ) |
| qwen2 | 72b-instruct-fp16-8cb4 | [HF Link](https://huggingface.co/Qwen/Qwen2-72B-Instruct) |
| qwen2 | 7b-instruct-awq-4bit-14aa | [HF Link](https://huggingface.co/Qwen/Qwen2-7B-Instruct-AWQ) |
| qwen2 | 7b-instruct-fp16-bbf2 | [HF Link](https://huggingface.co/Qwen/Qwen2-7B-Instruct) |

---


### Gemma <a id="gemma"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| gemma | 2b-instruct-fp16-6ee7 | [HF Link](https://huggingface.co/google/gemma-2b-it) |
| gemma | 7b-instruct-awq-4bit-df0b | [HF Link](https://huggingface.co/casperhansen/gemma-7b-it-awq) |
| gemma | 7b-instruct-fp16-2297 | [HF Link](https://huggingface.co/google/gemma-7b-it) |

---


### Llama-2 <a id="llama2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama2 | 13b-chat-fp16-ef61 | [HF Link](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) |
| llama2 | 70b-chat-fp16-16a0 | [HF Link](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) |
| llama2 | 7b-chat-awq-4bit-4f93 | [HF Link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-AWQ) |
| llama2 | 7b-chat-fp16-21b9 | [HF Link](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) |

---


### Mixtral <a id="mixtral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mixtral | 8x7b-instruct-v0.1-awq-4bit-06fd | [HF Link](https://huggingface.co/casperhansen/mixtral-instruct-awq) |
| mixtral | 8x7b-instruct-v0.1-fp16-e289 | [HF Link](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) |

---


### Mistral-Large <a id="mistral-large"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mistral-large | 123b-instruct-awq-4bit-1d37 | [HF Link](https://huggingface.co/casperhansen/mistral-large-instruct-2407-awq) |
| mistral-large | 123b-instruct-fp16-5c96 | [HF Link](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407) |

---


### Codestral <a id="codestral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| codestral | 22b-v0.1-fp16-12d3 | [HF Link](https://huggingface.co/mistralai/Codestral-22B-v0.1) |

---

