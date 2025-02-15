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
deepseek-r1          deepseek-r1:671b-fc3d                           default  80Gx16              linux
deepseek-r1-distill  deepseek-r1-distill:qwen2.5-14b-98a9            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-32b-9c8f            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-7b-math-fb74        default  24G                 linux
                     deepseek-r1-distill:llama3.1-8b-8c09            default  24G                 linux
                     deepseek-r1-distill:llama3.3-70b-instruct-31b8  default  80Gx2               linux
deepseek-v3          deepseek-v3:671b-instruct-d7ec                  default  80Gx16              linux
gemma2               gemma2:2b-instruct-747d                         default  12G                 linux
                     gemma2:9b-instruct-d9ad                         default  24G                 linux
                     gemma2:27b-instruct-8756                        default  80G                 linux
jamba1.5             jamba1.5:mini-d710                              default  80Gx4               linux
llama3.1             llama3.1:8b-instruct-3c0c                       default  24G                 linux
llama3.2             llama3.2:1b-instruct-f041                       default  24G                 linux
                     llama3.2:3b-instruct-3093                       default  24G                 linux
                     llama3.2:11b-vision-instruct-7bba               default  80G                 linux
                     llama3.2:90b-vision-instruct-c438               default  80Gx2               linux
llama3.3             llama3.3:70b-instruct-b850                      default  80Gx2               linux
mistral              mistral:8b-instruct-50e8                        default  24G                 linux
mistral-large        mistral-large:123b-instruct-1022                default  80Gx4               linux
                     mistral-large:123b-instruct-awq-4bit-38df       default  80G                 linux
mistralai            mistralai:24b-small-instruct-2501-0e69          default  80G                 linux
mixtral              mixtral:8x7b-instruct-v0.1-b752                 default  80Gx2               linux
phi4                 phi4:14b-c12d                                   default  80G                 linux
pixtral              pixtral:12b-240910-c344                         default  80G                 linux
qwen2.5              qwen2.5:7b-instruct-3260                        default  24G                 linux
                     qwen2.5:14b-instruct-39b4                       default  80G                 linux
                     qwen2.5:14b-instruct-ggml-q4-darwin-0f2e        default                      linux
                     qwen2.5:14b-instruct-ggml-q8-darwin-067c        default                      linux
                     qwen2.5:32b-instruct-285c                       default  80G                 linux
                     qwen2.5:32b-instruct-awq-4bit-eefb              default  40G                 linux
                     qwen2.5:32b-instruct-ggml-darwin-7ef9           default                      linux
                     qwen2.5:72b-instruct-0aa4                       default  80Gx2               linux
                     qwen2.5:72b-instruct-ggml-q4-darwin-143d        default                      linux
qwen2.5-coder        qwen2.5-coder:7b-instruct-e75d                  default  24G                 linux
                     qwen2.5-coder:7b-instruct-ggml-linux-d755       default                      linux
                     qwen2.5-coder:7b-instruct-ggml-darwin-3f22      default                      linux
                     qwen2.5-coder:32b-instruct-b814                 default  80G                 linux
qwen2.5vl            qwen2.5vl:3b-instruct-4686                      default  24G                 linux
                     qwen2.5vl:7b-instruct-c033                      default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.