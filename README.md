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
model                version                                         repo     required GPU RAM    platforms
-------------------  ----------------------------------------------  -------  ------------------  -----------
deepseek-r1          deepseek-r1:671b-a004                           default  80Gx16              linux
deepseek-r1-distill  deepseek-r1-distill:qwen2.5-14b-13b6            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-32b-db26            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-7b-math-b930        default  24G                 linux
                     deepseek-r1-distill:llama3.1-8b-3ab0            default  24G                 linux
                     deepseek-r1-distill:llama3.3-70b-instruct-1fc9  default  80Gx2               linux
deepseek-v3          deepseek-v3:671b-instruct-a3ae                  default  80Gx16              linux
gemma2               gemma2:2b-instruct-f239                         default  12G                 linux
                     gemma2:9b-instruct-42a7                         default  24G                 linux
                     gemma2:27b-instruct-d1f5                        default  80G                 linux
jamba1.5             jamba1.5:mini-4ece                              default  80Gx4               linux
llama3.1             llama3.1:8b-instruct-c522                       default  24G                 linux
llama3.2             llama3.2:11b-vision-instruct-6136               default  80G                 linux
llama3.3             llama3.3:70b-instruct-cbbe                      default  80Gx2               linux
mistral              mistral:8b-instruct-7621                        default  24G                 linux
mistral-large        mistral-large:123b-instruct-ba06                default  80Gx4               linux
                     mistral-large:123b-instruct-awq-4bit-11c2       default  80G                 linux
mistralai            mistralai:24b-small-instruct-2501-b455          default  80G                 linux
mixtral              mixtral:8x7b-instruct-v0.1-8be5                 default  80Gx2               linux
phi4                 phi4:14b-2eeb                                   default  80G                 linux
pixtral              pixtral:12b-240910-1b33                         default  80G                 linux
qwen2.5              qwen2.5:7b-instruct-d248                        default  24G                 linux
                     qwen2.5:14b-instruct-566a                       default  80G                 linux
                     qwen2.5:14b-instruct-ggml-q4-darwin-7a0b        default                      macos
                     qwen2.5:14b-instruct-ggml-q8-darwin-6fa0        default                      macos
                     qwen2.5:32b-instruct-0be9                       default  80G                 linux
                     qwen2.5:32b-instruct-awq-4bit-7474              default  40G                 linux
                     qwen2.5:32b-instruct-ggml-darwin-e457           default                      macos
                     qwen2.5:72b-instruct-e3ba                       default  80Gx2               linux
                     qwen2.5:72b-instruct-ggml-q4-darwin-ec8e        default                      macos
qwen2.5-coder        qwen2.5-coder:7b-instruct-3fbe                  default  24G                 linux
                     qwen2.5-coder:7b-instruct-ggml-linux-c347       default                      linux
                     qwen2.5-coder:7b-instruct-ggml-darwin-ba13      default                      macos
                     qwen2.5-coder:32b-instruct-c124                 default  80G                 linux
qwen2vl              qwen2vl:7b-instruct-137e                        default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.