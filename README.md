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
model                version                                              repo     required GPU RAM    platforms
-------------------  ---------------------------------------------------  -------  ------------------  -----------
codestral            codestral:22b-v0.1-fp16-7231                         default  80G                 linux
deepseek-r1-distill  deepseek-r1-distill:qwen2.5-14b-fp16-44c7            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-32b-fp16-29c6            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-7b-math-fp16-761e        default  24G                 linux
                     deepseek-r1-distill:qwen2.5-1.5b-math-fp16-5e2f      default  12G                 linux
                     deepseek-r1-distill:llama3.1-8b-fp16-f208            default  24G                 linux
                     deepseek-r1-distill:llama3.3-70b-instruct-fp16-5b46  default  80Gx2               linux
deepseek-v3          deepseek-v3:671b-instruct-fp8-70d7                   default  80Gx16              linux
gemma                gemma:2b-instruct-fp16-1320                          default  12G                 linux
                     gemma:7b-instruct-fp16-10bb                          default  24G                 linux
                     gemma:7b-instruct-awq-4bit-a9cb                      default  12G                 linux
gemma2               gemma2:9b-instruct-fp16-fdaa                         default  24G                 linux
                     gemma2:27b-instruct-fp16-c1e5                        default  80G                 linux
jamba1.5             jamba1.5:mini-fp16-3615                              default  80Gx4               linux
llama2               llama2:7b-chat-fp16-81cf                             default  16G                 linux
                     llama2:7b-chat-awq-4bit-cc6f                         default  12G                 linux
                     llama2:13b-chat-fp16-49e4                            default  40G                 linux
                     llama2:70b-chat-fp16-cc77                            default  80Gx2               linux
llama3               llama3:8b-instruct-fp16-9cf8                         default  24G                 linux
                     llama3:8b-instruct-awq-4bit-794a                     default  12G                 linux
                     llama3:70b-instruct-fp16-7265                        default  80Gx2               linux
                     llama3:70b-instruct-awq-4bit-f693                    default  80G                 linux
llama3.1             llama3.1:8b-instruct-fp16-cbdd                       default  24G                 linux
                     llama3.1:8b-instruct-awq-4bit-b149                   default  12G                 linux
                     llama3.1:70b-instruct-fp16-d198                      default  80Gx2               linux
                     llama3.1:70b-instruct-awq-4bit-e86e                  default  80G                 linux
                     llama3.1:405b-instruct-awq-4bit-bbd0                 default  80Gx4               linux
llama3.1-nemotron    llama3.1-nemotron:70b-instruct-fp16-8d09             default  80Gx2               linux
llama3.2             llama3.2:1b-instruct-fp16-ce2d                       default  12G                 linux
                     llama3.2:1b-instruct-ggml-fp16-linux-08c5            default                      linux
                     llama3.2:1b-instruct-ggml-fp16-darwin-12f1           default                      macos
                     llama3.2:3b-instruct-fp16-be73                       default  12G                 linux
                     llama3.2:11b-vision-instruct-714f                    default  80G                 linux
llama3.3             llama3.3:70b-instruct-fp16-419e                      default  80Gx2               linux
mistral              mistral:7b-instruct-fp16-26bd                        default  24G                 linux
                     mistral:7b-instruct-awq-4bit-ae66                    default  12G                 linux
                     mistral:24b-instruct-nemo-c545                       default  80G                 linux
mistral-large        mistral-large:123b-instruct-fp16-ce3a                default  80Gx4               linux
                     mistral-large:123b-instruct-awq-4bit-13a5            default  80G                 linux
mixtral              mixtral:8x7b-instruct-v0.1-fp16-04ce                 default  80Gx2               linux
                     mixtral:8x7b-instruct-v0.1-awq-4bit-4fc7             default  40G                 linux
phi3                 phi3:3.8b-instruct-fp16-d530                         default  12G                 linux
                     phi3:3.8b-instruct-ggml-q4-ccda                      default                      macos
phi4                 phi4:14b-fp16-b79c                                   default  80G                 linux
pixtral              pixtral:12b-240910-dd99                              default  80G                 linux
qwen2                qwen2:0.5b-instruct-fp16-750b                        default  12G                 linux
                     qwen2:1.5b-instruct-fp16-accb                        default  12G                 linux
                     qwen2:7b-instruct-fp16-7323                          default  24G                 linux
                     qwen2:7b-instruct-awq-4bit-8b5f                      default  12G                 linux
                     qwen2:57b-a14b-instruct-fp16-d5bd                    default  80Gx2               linux
                     qwen2:72b-instruct-fp16-7c3c                         default  80Gx2               linux
                     qwen2:72b-instruct-awq-4bit-2b3b                     default  80G                 linux
qwen2.5              qwen2.5:0.5b-instruct-fp16-7751                      default  12G                 linux
                     qwen2.5:1.5b-instruct-fp16-2705                      default  12G                 linux
                     qwen2.5:3b-instruct-fp16-047a                        default  12G                 linux
                     qwen2.5:7b-instruct-fp16-2c87                        default  24G                 linux
                     qwen2.5:14b-instruct-fp16-8019                       default  80G                 linux
                     qwen2.5:14b-instruct-ggml-q4-darwin-5f24             default                      macos
                     qwen2.5:14b-instruct-ggml-q8-darwin-8b4f             default                      macos
                     qwen2.5:32b-instruct-fp16-4839                       default  80G                 linux
                     qwen2.5:32b-instruct-awq-4bit-cc8d                   default  40G                 linux
                     qwen2.5:32b-instruct-ggml-fp16-darwin-028b           default                      macos
                     qwen2.5:72b-instruct-fp16-9475                       default  80Gx2               linux
                     qwen2.5:72b-instruct-ggml-q4-darwin-7e2c             default                      macos
qwen2.5-coder        qwen2.5-coder:7b-instruct-3c9a                       default  24G                 linux
                     qwen2.5-coder:7b-instruct-ggml-fp16-linux-6e86       default                      linux
                     qwen2.5-coder:7b-instruct-ggml-fp16-darwin-dc3a      default                      macos
                     qwen2.5-coder:32b-instruct-2ca2                      default  80G                 linux
qwen2vl              qwen2vl:7b-instruct-fp16-3da6                        default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.