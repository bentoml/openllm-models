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
model          version                                      repo     required GPU RAM    platforms
-------------  -------------------------------------------  -------  ------------------  -----------
deepseek       deepseek:r1-671b-e8f2                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-53c7         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-0b86         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-071e         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-8035        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-eeaf     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-380a    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-f20d    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-b6a2   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-f407   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-e313   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-6f2d  default  80G                 linux
               deepseek:v3-671b-9b31                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-f923                      default  12G                 linux
               gemma2:9b-instruct-f528                      default  24G                 linux
               gemma2:27b-instruct-a4e7                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-a246                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-672c         default  80Gx6               linux
jamba1.5       jamba1.5:large-d3da                          default  80Gx8               linux
               jamba1.5:mini-b8c3                           default  80Gx2               linux
llama3.1       llama3.1:8b-instruct-f130                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-39bf                    default  24G                 linux
               llama3.2:3b-instruct-2333                    default  24G                 linux
               llama3.2:11b-vision-instruct-d9e1            default  80G                 linux
               llama3.2:90b-vision-instruct-ecb9            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-cae9                   default  80Gx2               linux
mistral        mistral:8b-instruct-6447                     default  24G                 linux
               mistral:24b-small-instruct-2501-39e7         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-54f0        default  80Gx4               linux
phi4           phi4:14b-1cd5                                default  80G                 linux
pixtral        pixtral:12b-2409-1d8a                        default  80G                 linux
               pixtral:124b-2411-8fc7                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-c0ae                     default  24G                 linux
               qwen2.5:14b-instruct-b696                    default  80G                 linux
               qwen2.5:14b-instruct-awq-515a                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-267c          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-267c         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-910d     default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-4e26     default                      darwin
               qwen2.5:32b-instruct-ea3e                    default  80G                 linux
               qwen2.5:32b-instruct-awq-74c3                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-640f          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-8eca         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-7df9        default                      darwin
               qwen2.5:72b-instruct-69da                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-3c99                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-e608          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-2671         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-2ece     default                      darwin
qwen2.5-coder  qwen2.5-coder:3b-instruct-9508               default  24G                 linux
               qwen2.5-coder:7b-instruct-aaba               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-86e4           default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-d6c4    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-9351    default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a16-5abc    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-8a86   default                      darwin
               qwen2.5-coder:14b-instruct-1bec              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-4a59          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-a547    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-7923   default  40G                 linux
               qwen2.5-coder:32b-instruct-08a3              default  80G                 linux
qwq            qwq:32b-b853                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.