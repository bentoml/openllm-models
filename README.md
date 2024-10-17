<div align="center">
    <h1 align="center">The default model repository of <a href="https://github.com/bentoml/openllm">openllm</a></h1>
</div>

This repo (on `main` branch) is already included by openllm by default.

If you want more up-to-date untested models, please add our nightly branch.

```bash
openllm repo add nightly https://github.com/bentoml/openllm-models@nightly
```

## Supported Models
<table style="width: 100%; border-collapse: collapse;">
<tr>
  <td style="background-color: #D1D5DA; padding: 10px; border-radius: 8px 8px 0 0; width: 100%;">
    <span style="color: red;">●</span>
    <span style="color: yellow;">●</span>
    <span style="color: green;">●</span>
  </td>
</tr>
<tr>
<td>
        
```bash
$ openllm repo update
$ openllm model list
model          version                                     repo     required GPU RAM    platforms
-------------  ------------------------------------------  -------  ------------------  -----------
codestral      codestral:22b-v0.1-fp16-1802                default  80G                 linux
gemma          gemma:2b-instruct-fp16-f738                 default  12G                 linux
               gemma:7b-instruct-fp16-7ca0                 default  24G                 linux
               gemma:7b-instruct-awq-4bit-b214             default  12G                 linux
gemma2         gemma2:9b-instruct-fp16-e0c2                default  24G                 linux
               gemma2:27b-instruct-fp16-8ee8               default  80G                 linux
llama2         llama2:7b-chat-fp16-d7da                    default  16G                 linux
               llama2:7b-chat-awq-4bit-bad5                default  12G                 linux
               llama2:13b-chat-fp16-01e5                   default  40G                 linux
               llama2:70b-chat-fp16-fb96                   default  80Gx2               linux
llama3         llama3:8b-instruct-fp16-c11d                default  24G                 linux
               llama3:8b-instruct-awq-4bit-4c9c            default  12G                 linux
               llama3:70b-instruct-fp16-571d               default  80Gx2               linux
               llama3:70b-instruct-awq-4bit-a15f           default  80G                 linux
llama3.1       llama3.1:8b-instruct-fp16-79d3              default  24G                 linux
               llama3.1:8b-instruct-awq-4bit-522a          default  12G                 linux
               llama3.1:70b-instruct-fp16-859e             default  80Gx2               linux
               llama3.1:70b-instruct-awq-4bit-7cac         default  80G                 linux
               llama3.1:405b-instruct-awq-4bit-d543        default  80Gx4               linux
llama3.2       llama3.2:1b-instruct-fp16-dc66              default  12G                 linux
               llama3.2:1b-instruct-ggml-fp16-linux-3694   default                      linux
               llama3.2:1b-instruct-ggml-fp16-darwin-9fcb  default                      macos
               llama3.2:3b-instruct-fp16-6cc3              default  12G                 linux
               llama3.2:11b-vision-instruct-1459           default  80G                 linux
mistral        mistral:7b-instruct-fp16-31e6               default  24G                 linux
               mistral:7b-instruct-awq-4bit-0506           default  12G                 linux
               mistral:24b-instruct-nemo-9505              default  80G                 linux
mistral-large  mistral-large:123b-instruct-fp16-dd43       default  80Gx4               linux
               mistral-large:123b-instruct-awq-4bit-c5c3   default  80G                 linux
mixtral        mixtral:8x7b-instruct-v0.1-fp16-9bac        default  80Gx2               linux
               mixtral:8x7b-instruct-v0.1-awq-4bit-3eaf    default  40G                 linux
phi3           phi3:3.8b-instruct-fp16-7cdd                default  12G                 linux
               phi3:3.8b-instruct-ggml-q4-9c53             default                      macos
pixtral        pixtral:12b-240910-3480                     default  80G                 linux
qwen2          qwen2:0.5b-instruct-fp16-603d               default  12G                 linux
               qwen2:1.5b-instruct-fp16-8219               default  12G                 linux
               qwen2:7b-instruct-fp16-15ec                 default  24G                 linux
               qwen2:7b-instruct-awq-4bit-bb90             default  12G                 linux
               qwen2:57b-a14b-instruct-fp16-da51           default  80Gx2               linux
               qwen2:72b-instruct-fp16-02ba                default  80Gx2               linux
               qwen2:72b-instruct-awq-4bit-40e4            default  80G                 linux
qwen2.5        qwen2.5:0.5b-instruct-fp16-5ae4             default  12G                 linux
               qwen2.5:1.5b-instruct-fp16-0007             default  12G                 linux
               qwen2.5:3b-instruct-fp16-46fb               default  12G                 linux
               qwen2.5:7b-instruct-fp16-bc18               default  24G                 linux
               qwen2.5:14b-instruct-fp16-6fe3              default  80G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-5997    default                      macos
               qwen2.5:14b-instruct-ggml-q8-darwin-d0e8    default                      macos
               qwen2.5:32b-instruct-fp16-7848              default  80G                 linux
               qwen2.5:32b-instruct-ggml-fp16-darwin-00e1  default                      macos
               qwen2.5:72b-instruct-fp16-864f              default  80Gx2               linux
               qwen2.5:72b-instruct-ggml-q4-darwin-8b90    default                      macos

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.