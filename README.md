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
codestral      codestral:22b-v0.1-fp16-2638                default  80G                 linux
gemma          gemma:2b-instruct-fp16-d4c6                 default  12G                 linux
               gemma:7b-instruct-fp16-b15c                 default  24G                 linux
               gemma:7b-instruct-awq-4bit-464a             default  12G                 linux
gemma2         gemma2:9b-instruct-fp16-b9d3                default  24G                 linux
               gemma2:27b-instruct-fp16-9f48               default  80G                 linux
jamba1.5       jamba1.5:mini-fp16-9c32                     default  80Gx4               linux
llama2         llama2:7b-chat-fp16-3523                    default  16G                 linux
               llama2:7b-chat-awq-4bit-a536                default  12G                 linux
               llama2:13b-chat-fp16-b2a0                   default  40G                 linux
               llama2:70b-chat-fp16-7fe8                   default  80Gx2               linux
llama3         llama3:8b-instruct-fp16-07fd                default  24G                 linux
               llama3:8b-instruct-awq-4bit-da0a            default  12G                 linux
               llama3:70b-instruct-fp16-4863               default  80Gx2               linux
               llama3:70b-instruct-awq-4bit-c17d           default  80G                 linux
llama3.1       llama3.1:8b-instruct-fp16-d75d              default  24G                 linux
               llama3.1:8b-instruct-awq-4bit-96eb          default  12G                 linux
               llama3.1:70b-instruct-fp16-b86d             default  80Gx2               linux
               llama3.1:70b-instruct-awq-4bit-dbcc         default  80G                 linux
               llama3.1:405b-instruct-awq-4bit-2358        default  80Gx4               linux
llama3.2       llama3.2:1b-instruct-fp16-62c6              default  12G                 linux
               llama3.2:1b-instruct-ggml-fp16-linux-60fa   default                      linux
               llama3.2:1b-instruct-ggml-fp16-darwin-8d35  default                      macos
               llama3.2:3b-instruct-fp16-53eb              default  12G                 linux
               llama3.2:11b-vision-instruct-8926           default  80G                 linux
mistral        mistral:7b-instruct-fp16-6aea               default  24G                 linux
               mistral:7b-instruct-awq-4bit-1bf8           default  12G                 linux
               mistral:24b-instruct-nemo-9adb              default  80G                 linux
mistral-large  mistral-large:123b-instruct-fp16-9008       default  80Gx4               linux
               mistral-large:123b-instruct-awq-4bit-377e   default  80G                 linux
mixtral        mixtral:8x7b-instruct-v0.1-fp16-b8de        default  80Gx2               linux
               mixtral:8x7b-instruct-v0.1-awq-4bit-1392    default  40G                 linux
phi3           phi3:3.8b-instruct-fp16-ac3c                default  12G                 linux
               phi3:3.8b-instruct-ggml-q4-463e             default                      macos
pixtral        pixtral:12b-240910-82ad                     default  80G                 linux
qwen2          qwen2:0.5b-instruct-fp16-fe8a               default  12G                 linux
               qwen2:1.5b-instruct-fp16-74cd               default  12G                 linux
               qwen2:7b-instruct-fp16-e8fa                 default  24G                 linux
               qwen2:7b-instruct-awq-4bit-dc8b             default  12G                 linux
               qwen2:57b-a14b-instruct-fp16-55df           default  80Gx2               linux
               qwen2:72b-instruct-fp16-5ba6                default  80Gx2               linux
               qwen2:72b-instruct-awq-4bit-2907            default  80G                 linux
qwen2.5        qwen2.5:0.5b-instruct-fp16-d59e             default  12G                 linux
               qwen2.5:1.5b-instruct-fp16-d1e9             default  12G                 linux
               qwen2.5:3b-instruct-fp16-b569               default  12G                 linux
               qwen2.5:7b-instruct-fp16-60be               default  24G                 linux
               qwen2.5:14b-instruct-fp16-9539              default  80G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-1cf2    default                      macos
               qwen2.5:14b-instruct-ggml-q8-darwin-f06a    default                      macos
               qwen2.5:32b-instruct-fp16-7b67              default  80G                 linux
               qwen2.5:32b-instruct-awq-4bit-6958          default  40G                 linux
               qwen2.5:32b-instruct-ggml-fp16-darwin-809c  default                      macos
               qwen2.5:72b-instruct-fp16-aa9c              default  80Gx2               linux
               qwen2.5:72b-instruct-ggml-q4-darwin-a138    default                      macos
qwen2vl        qwen2vl:7b-instruct-fp16-8a12               default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.