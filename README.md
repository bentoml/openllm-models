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
deepseek-r1          deepseek-r1:671b-6bfb                           default  80Gx16              linux
deepseek-r1-distill  deepseek-r1-distill:qwen2.5-14b-258d            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-32b-68aa            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-7b-math-fe2d        default  24G                 linux
                     deepseek-r1-distill:llama3.1-8b-b99a            default  24G                 linux
                     deepseek-r1-distill:llama3.3-70b-instruct-09ea  default  80Gx2               linux
deepseek-v3          deepseek-v3:671b-instruct-c440                  default  80Gx16              linux
gemma2               gemma2:9b-instruct-9223                         default  24G                 linux
                     gemma2:27b-instruct-bfcb                        default  80G                 linux
jamba1.5             jamba1.5:mini-6d5d                              default  80Gx4               linux
llama3.1             llama3.1:8b-instruct-e11a                       default  24G                 linux
llama3.2             llama3.2:11b-vision-instruct-30a6               default  80G                 linux
llama3.3             llama3.3:70b-instruct-8722                      default  80Gx2               linux
mistral              mistral:8b-instruct-2892                        default  24G                 linux
mistral-large        mistral-large:123b-instruct-1073                default  80Gx4               linux
                     mistral-large:123b-instruct-awq-4bit-63c0       default  80G                 linux
mistralai            mistralai:24b-small-instruct-2501-a04a          default  80G                 linux
mixtral              mixtral:8x7b-instruct-v0.1-3998                 default  80Gx2               linux
phi4                 phi4:14b-240d                                   default  80G                 linux
pixtral              pixtral:12b-240910-c0c3                         default  80G                 linux
qwen2.5              qwen2.5:7b-instruct-1512                        default  24G                 linux
                     qwen2.5:14b-instruct-72a9                       default  80G                 linux
                     qwen2.5:14b-instruct-ggml-q4-darwin-7a0b        default                      macos
                     qwen2.5:14b-instruct-ggml-q8-darwin-6fa0        default                      macos
                     qwen2.5:32b-instruct-25e4                       default  80G                 linux
                     qwen2.5:32b-instruct-awq-4bit-4b27              default  40G                 linux
                     qwen2.5:32b-instruct-ggml-darwin-e457           default                      macos
                     qwen2.5:72b-instruct-33e6                       default  80Gx2               linux
                     qwen2.5:72b-instruct-ggml-q4-darwin-ec8e        default                      macos
qwen2.5-coder        qwen2.5-coder:7b-instruct-5f58                  default  24G                 linux
                     qwen2.5-coder:7b-instruct-ggml-linux-c347       default                      linux
                     qwen2.5-coder:7b-instruct-ggml-darwin-ba13      default                      macos
                     qwen2.5-coder:32b-instruct-4153                 default  80G                 linux
qwen2vl              qwen2vl:7b-instruct-b8c4                        default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.