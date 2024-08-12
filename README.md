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
- [](#mistral-large)

---


### Llama-3.1 <a id="llama3.1"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama3.1 | 405b-instruct-awq-4bit-675e | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-405B-Instruct-AWQ-INT4) |
| llama3.1 | 70b-instruct-awq-4bit-28ed | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4) |
| llama3.1 | 70b-instruct-fp16-b66b | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) |
| llama3.1 | 8b-instruct-awq-4bit-5cb2 | [HF Link](https://huggingface.co/hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4) |
| llama3.1 | 8b-instruct-fp16-1c1c | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) |

---


### Llama-3 <a id="llama3"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama3 | 70b-instruct-awq-4bit-9ceb | [HF Link](https://huggingface.co/casperhansen/llama-3-70b-instruct-awq) |
| llama3 | 70b-instruct-fp16-c3e4 | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) |
| llama3 | 8b-instruct-awq-4bit-1c94 | [HF Link](https://huggingface.co/casperhansen/llama-3-8b-instruct-awq) |
| llama3 | 8b-instruct-fp16-ba7c | [HF Link](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) |

---


### Phi-3 <a id="phi3"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| phi3 | 3.8b-instruct-fp16-37b9 | [HF Link](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) |
| phi3 | 3.8b-instruct-ggml-q4-cf55 | [HF Link](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf) |

---


### Mistral <a id="mistral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mistral | 7b-instruct-awq-4bit-4406 | [HF Link](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-AWQ) |
| mistral | 7b-instruct-fp16-e3bd | [HF Link](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) |

---


### Gemma-2 <a id="gemma2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| gemma2 | 27b-instruct-fp16-9799 | [HF Link](https://huggingface.co/google/gemma-2-27b-it) |
| gemma2 | 9b-instruct-fp16-cb2b | [HF Link](https://huggingface.co/google/gemma-2-9b-it) |

---


### Qwen-2 <a id="qwen2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| qwen2 | 0.5b-instruct-fp16-bca0 | [HF Link](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct) |
| qwen2 | 1.5b-instruct-fp16-df66 | [HF Link](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct) |
| qwen2 | 57b-a14b-instruct-fp16-b847 | [HF Link](https://huggingface.co/Qwen/Qwen2-57B-A14B-Instruct) |
| qwen2 | 72b-instruct-awq-4bit-60b1 | [HF Link](https://huggingface.co/Qwen/Qwen2-72B-Instruct-AWQ) |
| qwen2 | 72b-instruct-fp16-ee8e | [HF Link](https://huggingface.co/Qwen/Qwen2-72B-Instruct) |
| qwen2 | 7b-instruct-awq-4bit-02f4 | [HF Link](https://huggingface.co/Qwen/Qwen2-7B-Instruct-AWQ) |
| qwen2 | 7b-instruct-fp16-761c | [HF Link](https://huggingface.co/Qwen/Qwen2-7B-Instruct) |

---


### Gemma <a id="gemma"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| gemma | 2b-instruct-fp16-f6ee | [HF Link](https://huggingface.co/google/gemma-2b-it) |
| gemma | 7b-instruct-awq-4bit-bdb5 | [HF Link](https://huggingface.co/casperhansen/gemma-7b-it-awq) |
| gemma | 7b-instruct-fp16-35e0 | [HF Link](https://huggingface.co/google/gemma-7b-it) |

---


### Llama-2 <a id="llama2"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| llama2 | 13b-chat-fp16-a846 | [HF Link](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) |
| llama2 | 70b-chat-fp16-fcef | [HF Link](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) |
| llama2 | 7b-chat-awq-4bit-753b | [HF Link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-AWQ) |
| llama2 | 7b-chat-fp16-dc53 | [HF Link](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) |

---


### Mixtral <a id="mixtral"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mixtral | 8x7b-instruct-v0.1-awq-4bit-7bae | [HF Link](https://huggingface.co/casperhansen/mixtral-instruct-awq) |
| mixtral | 8x7b-instruct-v0.1-fp16-1c82 | [HF Link](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) |

---


###  <a id="mistral-large"></a>

| Model | Version | Huggingface Link |
| --- | --- | --- |
| mistral-large | 123b-instruct-awq-4bit-c380 | [HF Link](https://huggingface.co/casperhansen/mistral-large-instruct-2407-awq) |
| mistral-large | 123b-instruct-fp16-a203 | [HF Link](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407) |

---

