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
deepseek-r1          deepseek-r1:671b-94e3                           default  80Gx16              linux
deepseek-r1-distill  deepseek-r1-distill:qwen2.5-14b-c378            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-32b-ebe6            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-7b-math-867a        default  24G                 linux
                     deepseek-r1-distill:llama3.1-8b-10f5            default  24G                 linux
                     deepseek-r1-distill:llama3.3-70b-instruct-4cc4  default  80Gx2               linux
deepseek-v3          deepseek-v3:671b-instruct-f864                  default  80Gx16              linux
gemma2               gemma2:2b-instruct-c097                         default  12G                 linux
                     gemma2:9b-instruct-dcca                         default  24G                 linux
                     gemma2:27b-instruct-e641                        default  80G                 linux
jamba1.5             jamba1.5:mini-48e1                              default  80Gx4               linux
llama3.1             llama3.1:8b-instruct-189d                       default  24G                 linux
llama3.2             llama3.2:1b-instruct-67fd                       default  24G                 linux
                     llama3.2:3b-instruct-2068                       default  24G                 linux
                     llama3.2:11b-vision-instruct-707b               default  80G                 linux
                     llama3.2:90b-vision-instruct-4b39               default  80Gx2               linux
llama3.3             llama3.3:70b-instruct-b1a2                      default  80Gx2               linux
mistral              mistral:8b-instruct-3b47                        default  24G                 linux
mistral-large        mistral-large:123b-instruct-a8d3                default  80Gx4               linux
                     mistral-large:123b-instruct-awq-4bit-21b9       default  80G                 linux
mistralai            mistralai:24b-small-instruct-2501-cb86          default  80G                 linux
mixtral              mixtral:8x7b-instruct-v0.1-bc8d                 default  80Gx2               linux
phi4                 phi4:14b-8ca1                                   default  80G                 linux
pixtral              pixtral:12b-240910-b02b                         default  80G                 linux
qwen2.5              qwen2.5:7b-instruct-e221                        default  24G                 linux
                     qwen2.5:14b-instruct-bba4                       default  80G                 linux
                     qwen2.5:14b-instruct-ggml-q4-darwin-7a0b        default                      macos
                     qwen2.5:14b-instruct-ggml-q8-darwin-6fa0        default                      macos
                     qwen2.5:32b-instruct-ac25                       default  80G                 linux
                     qwen2.5:32b-instruct-awq-4bit-f93b              default  40G                 linux
                     qwen2.5:32b-instruct-ggml-darwin-e457           default                      macos
                     qwen2.5:72b-instruct-986a                       default  80Gx2               linux
                     qwen2.5:72b-instruct-ggml-q4-darwin-ec8e        default                      macos
qwen2.5-coder        qwen2.5-coder:7b-instruct-b419                  default  24G                 linux
                     qwen2.5-coder:7b-instruct-ggml-linux-c347       default                      linux
                     qwen2.5-coder:7b-instruct-ggml-darwin-ba13      default                      macos
                     qwen2.5-coder:32b-instruct-f557                 default  80G                 linux
qwen2vl              qwen2vl:7b-instruct-8d74                        default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.