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
codestral            codestral:22b-v0.1-fp16-eb81                         default  80G                 linux
deepseek-r1-distill  deepseek-r1-distill:qwen2.5-14b-fp16-55a4            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-32b-fp16-323e            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-7b-math-fp16-e42d        default  24G                 linux
                     deepseek-r1-distill:qwen2.5-1.5b-math-fp16-53ee      default  12G                 linux
                     deepseek-r1-distill:llama3.1-8b-fp16-9428            default  24G                 linux
                     deepseek-r1-distill:llama3.3-70b-instruct-fp16-03c5  default  80Gx2               linux
deepseek-v3          deepseek-v3:671b-instruct-fp8-6e62                   default  80Gx16              linux
gemma                gemma:2b-instruct-fp16-51c1                          default  12G                 linux
                     gemma:7b-instruct-fp16-c9be                          default  24G                 linux
                     gemma:7b-instruct-awq-4bit-f9f8                      default  12G                 linux
gemma2               gemma2:9b-instruct-fp16-bf10                         default  24G                 linux
                     gemma2:27b-instruct-fp16-f2fd                        default  80G                 linux
jamba1.5             jamba1.5:mini-fp16-82d1                              default  80Gx4               linux
llama2               llama2:7b-chat-fp16-e426                             default  16G                 linux
                     llama2:7b-chat-awq-4bit-c3b0                         default  12G                 linux
                     llama2:13b-chat-fp16-e54f                            default  40G                 linux
                     llama2:70b-chat-fp16-acda                            default  80Gx2               linux
llama3               llama3:8b-instruct-fp16-63ae                         default  24G                 linux
                     llama3:8b-instruct-awq-4bit-824a                     default  12G                 linux
                     llama3:70b-instruct-fp16-7240                        default  80Gx2               linux
                     llama3:70b-instruct-awq-4bit-cf0f                    default  80G                 linux
llama3.1             llama3.1:8b-instruct-fp16-d57d                       default  24G                 linux
                     llama3.1:8b-instruct-awq-4bit-c3e1                   default  12G                 linux
                     llama3.1:70b-instruct-fp16-10cf                      default  80Gx2               linux
                     llama3.1:70b-instruct-awq-4bit-5148                  default  80G                 linux
                     llama3.1:405b-instruct-awq-4bit-f4b5                 default  80Gx4               linux
llama3.1-nemotron    llama3.1-nemotron:70b-instruct-fp16-32aa             default  80Gx2               linux
llama3.2             llama3.2:1b-instruct-fp16-36e6                       default  12G                 linux
                     llama3.2:1b-instruct-ggml-fp16-linux-08c5            default                      linux
                     llama3.2:1b-instruct-ggml-fp16-darwin-12f1           default                      macos
                     llama3.2:3b-instruct-fp16-c4b1                       default  12G                 linux
                     llama3.2:11b-vision-instruct-271d                    default  80G                 linux
llama3.3             llama3.3:70b-instruct-fp16-712f                      default  80Gx2               linux
mistral              mistral:7b-instruct-fp16-46a4                        default  24G                 linux
                     mistral:7b-instruct-awq-4bit-d1c0                    default  12G                 linux
                     mistral:24b-instruct-nemo-e4cb                       default  80G                 linux
mistral-large        mistral-large:123b-instruct-fp16-c555                default  80Gx4               linux
                     mistral-large:123b-instruct-awq-4bit-9d8d            default  80G                 linux
mixtral              mixtral:8x7b-instruct-v0.1-fp16-4a8e                 default  80Gx2               linux
                     mixtral:8x7b-instruct-v0.1-awq-4bit-b202             default  40G                 linux
phi3                 phi3:3.8b-instruct-fp16-f21c                         default  12G                 linux
                     phi3:3.8b-instruct-ggml-q4-ccda                      default                      macos
phi4                 phi4:14b-fp16-6ba5                                   default  80G                 linux
pixtral              pixtral:12b-240910-929b                              default  80G                 linux
qwen2                qwen2:0.5b-instruct-fp16-e673                        default  12G                 linux
                     qwen2:1.5b-instruct-fp16-9bce                        default  12G                 linux
                     qwen2:7b-instruct-fp16-dc40                          default  24G                 linux
                     qwen2:7b-instruct-awq-4bit-239b                      default  12G                 linux
                     qwen2:57b-a14b-instruct-fp16-441d                    default  80Gx2               linux
                     qwen2:72b-instruct-fp16-5549                         default  80Gx2               linux
                     qwen2:72b-instruct-awq-4bit-0e35                     default  80G                 linux
qwen2.5              qwen2.5:0.5b-instruct-fp16-01b9                      default  12G                 linux
                     qwen2.5:1.5b-instruct-fp16-3f28                      default  12G                 linux
                     qwen2.5:3b-instruct-fp16-502e                        default  12G                 linux
                     qwen2.5:7b-instruct-fp16-d5ae                        default  24G                 linux
                     qwen2.5:14b-instruct-fp16-7fd4                       default  80G                 linux
                     qwen2.5:14b-instruct-ggml-q4-darwin-5f24             default                      macos
                     qwen2.5:14b-instruct-ggml-q8-darwin-8b4f             default                      macos
                     qwen2.5:32b-instruct-fp16-d2bf                       default  80G                 linux
                     qwen2.5:32b-instruct-awq-4bit-f7bc                   default  40G                 linux
                     qwen2.5:32b-instruct-ggml-fp16-darwin-028b           default                      macos
                     qwen2.5:72b-instruct-fp16-e4a2                       default  80Gx2               linux
                     qwen2.5:72b-instruct-ggml-q4-darwin-7e2c             default                      macos
qwen2.5-coder        qwen2.5-coder:7b-instruct-9748                       default  24G                 linux
                     qwen2.5-coder:7b-instruct-ggml-fp16-linux-6e86       default                      linux
                     qwen2.5-coder:7b-instruct-ggml-fp16-darwin-dc3a      default                      macos
                     qwen2.5-coder:32b-instruct-3e56                      default  80G                 linux
qwen2vl              qwen2vl:7b-instruct-fp16-94e0                        default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.