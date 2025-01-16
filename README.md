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
model              version                                          repo     required GPU RAM    platforms
-----------------  -----------------------------------------------  -------  ------------------  -----------
codestral          codestral:22b-v0.1-fp16-f863                     default  80G                 linux
deepseek-v3        deepseek-v3:671b-instruct-fp8-1b06               default  80Gx16              linux
gemma              gemma:2b-instruct-fp16-ee71                      default  12G                 linux
                   gemma:7b-instruct-fp16-57f3                      default  24G                 linux
                   gemma:7b-instruct-awq-4bit-c24c                  default  12G                 linux
gemma2             gemma2:9b-instruct-fp16-acb4                     default  24G                 linux
                   gemma2:27b-instruct-fp16-f59b                    default  80G                 linux
jamba1.5           jamba1.5:mini-fp16-7a80                          default  80Gx4               linux
llama2             llama2:7b-chat-fp16-9743                         default  16G                 linux
                   llama2:7b-chat-awq-4bit-dca8                     default  12G                 linux
                   llama2:13b-chat-fp16-2278                        default  40G                 linux
                   llama2:70b-chat-fp16-8cf8                        default  80Gx2               linux
llama3             llama3:8b-instruct-fp16-53c7                     default  24G                 linux
                   llama3:8b-instruct-awq-4bit-6a62                 default  12G                 linux
                   llama3:70b-instruct-fp16-780e                    default  80Gx2               linux
                   llama3:70b-instruct-awq-4bit-7b7a                default  80G                 linux
llama3.1           llama3.1:8b-instruct-fp16-44ee                   default  24G                 linux
                   llama3.1:8b-instruct-awq-4bit-5f20               default  12G                 linux
                   llama3.1:70b-instruct-fp16-1fbd                  default  80Gx2               linux
                   llama3.1:70b-instruct-awq-4bit-729e              default  80G                 linux
                   llama3.1:405b-instruct-awq-4bit-f53c             default  80Gx4               linux
llama3.1-nemotron  llama3.1-nemotron:70b-instruct-fp16-c65f         default  80Gx2               linux
llama3.2           llama3.2:1b-instruct-fp16-b511                   default  12G                 linux
                   llama3.2:1b-instruct-ggml-fp16-linux-08c5        default                      linux
                   llama3.2:1b-instruct-ggml-fp16-darwin-12f1       default                      macos
                   llama3.2:3b-instruct-fp16-dd11                   default  12G                 linux
                   llama3.2:11b-vision-instruct-4e4c                default  80G                 linux
llama3.3           llama3.3:70b-instruct-fp16-b9d2                  default  80Gx2               linux
mistral            mistral:7b-instruct-fp16-6dd3                    default  24G                 linux
                   mistral:7b-instruct-awq-4bit-45a4                default  12G                 linux
                   mistral:24b-instruct-nemo-4517                   default  80G                 linux
mistral-large      mistral-large:123b-instruct-fp16-6694            default  80Gx4               linux
                   mistral-large:123b-instruct-awq-4bit-6ab7        default  80G                 linux
mixtral            mixtral:8x7b-instruct-v0.1-fp16-a0e4             default  80Gx2               linux
                   mixtral:8x7b-instruct-v0.1-awq-4bit-bdce         default  40G                 linux
phi3               phi3:3.8b-instruct-fp16-a842                     default  12G                 linux
                   phi3:3.8b-instruct-ggml-q4-ccda                  default                      macos
phi4               phi4:14b-fp16-9bdd                               default  80G                 linux
pixtral            pixtral:12b-240910-9ad6                          default  80G                 linux
qwen2              qwen2:0.5b-instruct-fp16-e49c                    default  12G                 linux
                   qwen2:1.5b-instruct-fp16-e104                    default  12G                 linux
                   qwen2:7b-instruct-fp16-d9a9                      default  24G                 linux
                   qwen2:7b-instruct-awq-4bit-1bd2                  default  12G                 linux
                   qwen2:57b-a14b-instruct-fp16-072b                default  80Gx2               linux
                   qwen2:72b-instruct-fp16-ca54                     default  80Gx2               linux
                   qwen2:72b-instruct-awq-4bit-0c39                 default  80G                 linux
qwen2.5            qwen2.5:0.5b-instruct-fp16-1358                  default  12G                 linux
                   qwen2.5:1.5b-instruct-fp16-2ea9                  default  12G                 linux
                   qwen2.5:3b-instruct-fp16-631c                    default  12G                 linux
                   qwen2.5:7b-instruct-fp16-246c                    default  24G                 linux
                   qwen2.5:14b-instruct-fp16-a9c1                   default  80G                 linux
                   qwen2.5:14b-instruct-ggml-q4-darwin-5f24         default                      macos
                   qwen2.5:14b-instruct-ggml-q8-darwin-8b4f         default                      macos
                   qwen2.5:32b-instruct-fp16-e713                   default  80G                 linux
                   qwen2.5:32b-instruct-awq-4bit-251b               default  40G                 linux
                   qwen2.5:32b-instruct-ggml-fp16-darwin-028b       default                      macos
                   qwen2.5:72b-instruct-fp16-a451                   default  80Gx2               linux
                   qwen2.5:72b-instruct-ggml-q4-darwin-7e2c         default                      macos
qwen2.5-coder      qwen2.5-coder:7b-instruct-b3f0                   default  24G                 linux
                   qwen2.5-coder:7b-instruct-ggml-fp16-linux-6e86   default                      linux
                   qwen2.5-coder:7b-instruct-ggml-fp16-darwin-dc3a  default                      macos
                   qwen2.5-coder:32b-instruct-16b6                  default  80G                 linux
qwen2vl            qwen2vl:7b-instruct-fp16-8f80                    default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.