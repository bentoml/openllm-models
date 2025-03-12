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
deepseek       deepseek:r1                                 default  80Gx16              linux
               deepseek:r1-llama3.1-8b                     default  24G                 linux
               deepseek:r1-qwen2.5-14b                     default  80G                 linux
               deepseek:r1-qwen2.5-32b                     default  80G                 linux
               deepseek:r1-llama3.3-70b                    default  80Gx2               linux
               deepseek:r1-qwen2.5-math                    default  24G                 linux
               deepseek:r1-qwen2.5-14b-w8a8                default  24G                 linux
               deepseek:r1-qwen2.5-32b-w8a8                default  80G                 linux
               deepseek:r1-llama3.3-70b-w8a8               default  80G                 linux
               deepseek:r1-qwen2.5-14b-w4a16               default  24G                 linux
               deepseek:r1-qwen2.5-32b-w4a16               default  80G                 linux
               deepseek:r1-llama3.3-70b-w4a16              default  80G                 linux
               deepseek:v3                                 default  80Gx16              linux
gemma2         gemma2:2b                                   default  12G                 linux
               gemma2:9b                                   default  24G                 linux
               gemma2:27b                                  default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-3622                default  80G                 linux
               hermes-3:llama3.1-405b-instruct-bef1        default  80Gx6               linux
jamba1.5       jamba1.5:mini-5e51                          default  80Gx2               linux
               jamba1.5:large                              default  80Gx8               linux
llama3.1       llama3.1:8b                                 default  24G                 linux
llama3.2       llama3.2:1b                                 default  24G                 linux
               llama3.2:3b                                 default  24G                 linux
               llama3.2:11b                                default  80G                 linux
               llama3.2:90b                                default  80Gx2               linux
llama3.3       llama3.3:70b                                default  80Gx2               linux
mistral        mistral:8b                                  default  24G                 linux
               mistral:24b                                 default  80G                 linux
mistral-large  mistral-large:123b                          default  80Gx4               linux
phi4           phi4:14b                                    default  80G                 linux
pixtral        pixtral:12b-2409                            default  80G                 linux
               pixtral:124b                                default  80Gx4               linux
qwen2.5        qwen2.5:7b                                  default  24G                 linux
               qwen2.5:14b                                 default  80G                 linux
               qwen2.5:14b-awq                             default  24G                 linux
               qwen2.5:14b-w4a8                            default  24G                 linux
               qwen2.5:14b-w4a16                           default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-910d    default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-4e26    default                      darwin
               qwen2.5:32b                                 default  80G                 linux
               qwen2.5:32b-awq                             default  40G                 linux
               qwen2.5:32b-w8a8                            default  40G                 linux
               qwen2.5:32b-w4a16                           default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-7df9       default                      darwin
               qwen2.5:72b                                 default  80G                 linux
               qwen2.5:72b-w8a8                            default  80G                 linux
               qwen2.5:72b-w4a16                           default  80G                 linux
               qwen2.5:72b-instruct-4c9a                   default  80Gx2               linux
               qwen2.5:72b-instruct-ggml-q4-darwin-2ece    default                      darwin
qwen2.5-coder  qwen2.5-coder:3b                            default  24G                 linux
               qwen2.5-coder:7b                            default  24G                 linux
               qwen2.5-coder:7b-awq                        default  24G                 linux
               qwen2.5-coder:7b-w8a8                       default  24G                 linux
               qwen2.5-coder:7b-w4a16                      default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-d6c4   default                      linux
               qwen2.5-coder:7b-instruct-ggml-darwin-8a86  default                      darwin
               qwen2.5-coder:14b                           default  40G                 linux
               qwen2.5-coder:14b-awq                       default  40G                 linux
               qwen2.5-coder:14b-w8a8                      default  40G                 linux
               qwen2.5-coder:14b-w4a16                     default  40G                 linux
               qwen2.5-coder:32b                           default  80G                 linux
qwq            qwq:32b                                     default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.