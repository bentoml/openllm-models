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

- [Llama-3.2](#llama3.2)
- [Qwen-2.5](#qwen2.5)
- [Pixtral](#pixtral)
- [Phi-3](#phi3)
- [Mistral](#mistral)
- [Gemma-2](#gemma2)
- [Mixtral](#mixtral)
- [Mistral-Large](#mistral-large)
- [Codestral](#codestral)
- [Llama-3](#llama3)
- [Qwen-2](#qwen2)
- [Llama-3.1](#llama3.1)
- [Llama-2](#llama2)
- [Gemma](#gemma)

---


### Llama-3.2 <a id="llama3.2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama3.2 | 11b-vision-instruct | [HF Link](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) |
| llama3.2 | 1b-instruct-fp16 | [HF Link](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) |
| llama3.2 | 3b-instruct-fp16 | [HF Link](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) |

---


### Qwen-2.5 <a id="qwen2.5"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| qwen2.5 | 0.5b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) |
| qwen2.5 | 1.5b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) |
| qwen2.5 | 14b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) |
| qwen2.5 | 32b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) |
| qwen2.5 | 3b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) |
| qwen2.5 | 72b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) |
| qwen2.5 | 7b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) |

---


### Pixtral <a id="pixtral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| pixtral | 12b-240910 | [HF Link](https://huggingface.co/mistral-community/pixtral-12b-240910) |

---


### Phi-3 <a id="phi3"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| phi3 | 3.8b-instruct-fp16 | [HF Link](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) |
| phi3 | 3.8b-instruct-ggml-q4 | [HF Link](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf) |

---


### Mistral <a id="mistral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mistral | 24b-instruct-nemo | [HF Link](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) |
| mistral | 7b-instruct-awq-4bit | [HF Link](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-AWQ) |
| mistral | 7b-instruct-fp16 | [HF Link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) |

---


### Gemma-2 <a id="gemma2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| gemma2 | 27b-instruct-fp16 | [HF Link](https://huggingface.co/google/gemma-2-27b-it) |
| gemma2 | 9b-instruct-fp16 | [HF Link](https://huggingface.co/google/gemma-2-9b-it) |

---


### Mixtral <a id="mixtral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mixtral | 8x7b-instruct-v0.1-awq-4bit | [HF Link](https://huggingface.co/casperhansen/mixtral-instruct-awq) |
| mixtral | 8x7b-instruct-v0.1-fp16 | [HF Link](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) |

---


### Mistral-Large <a id="mistral-large"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mistral-large | 123b-instruct-awq-4bit | [HF Link](https://huggingface.co/casperhansen/mistral-large-instruct-2407-awq) |
| mistral-large | 123b-instruct-fp16 | [HF Link](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407) |

---


### Codestral <a id="codestral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| codestral | 22b-v0.1-fp16 | [HF Link](https://huggingface.co/mistralai/Codestral-22B-v0.1) |

---


### Llama-3 <a id="llama3"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama3 | 70b-instruct-awq-4bit | [HF Link](https://huggingface.co/casperhansen/llama-3-70b-instruct-awq) |
| llama3 | 70b-instruct-fp16 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) |
| llama3 | 8b-instruct-awq-4bit | [HF Link](https://huggingface.co/casperhansen/llama-3-8b-instruct-awq) |
| llama3 | 8b-instruct-fp16 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) |

---


### Qwen-2 <a id="qwen2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| qwen2 | 0.5b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct) |
| qwen2 | 1.5b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct) |
| qwen2 | 57b-a14b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2-57B-A14B-Instruct) |
| qwen2 | 72b-instruct-awq-4bit | [HF Link](https://huggingface.co/Qwen/Qwen2-72B-Instruct-AWQ) |
| qwen2 | 72b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2-72B-Instruct) |
| qwen2 | 7b-instruct-awq-4bit | [HF Link](https://huggingface.co/Qwen/Qwen2-7B-Instruct-AWQ) |
| qwen2 | 7b-instruct-fp16 | [HF Link](https://huggingface.co/Qwen/Qwen2-7B-Instruct) |

---


### Llama-3.1 <a id="llama3.1"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama3.1 | 405b-instruct-awq-4bit | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-405B-Instruct-AWQ-INT4) |
| llama3.1 | 70b-instruct-awq-4bit | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4) |
| llama3.1 | 70b-instruct-fp16 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) |
| llama3.1 | 8b-instruct-awq-4bit | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4) |
| llama3.1 | 8b-instruct-fp16 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) |

---


### Llama-2 <a id="llama2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama2 | 13b-chat-fp16 | [HF Link](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) |
| llama2 | 70b-chat-fp16 | [HF Link](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) |
| llama2 | 7b-chat-awq-4bit | [HF Link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-AWQ) |
| llama2 | 7b-chat-fp16 | [HF Link](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) |

---


### Gemma <a id="gemma"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| gemma | 2b-instruct-fp16 | [HF Link](https://huggingface.co/google/gemma-2b-it) |
| gemma | 7b-instruct-awq-4bit | [HF Link](https://huggingface.co/casperhansen/gemma-7b-it-awq) |
| gemma | 7b-instruct-fp16 | [HF Link](https://huggingface.co/google/gemma-7b-it) |

---

