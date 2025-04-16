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
deepseek       deepseek:r1-671b-0dc9                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-67ab         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-98b3         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-3803         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-62f7        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-2851     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-65b0    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-9a8d    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-f771   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-7277   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-7144   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-60b5  default  80G                 linux
               deepseek:v3-671b-b489                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-8ed1                      default  12G                 linux
               gemma2:9b-instruct-e443                      default  24G                 linux
               gemma2:27b-instruct-241c                     default  80G                 linux
gemma3         gemma3:1b-instruct-227e                      default  12G                 linux
               gemma3:4b-instruct-17bf                      default  24G                 linux
               gemma3:12b-instruct-f081                     default  40G                 linux
               gemma3:27b-instruct-8e0b                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-5377                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-247a         default  80Gx8               linux
jamba1.5       jamba1.5:mini-5a33                           default  80Gx2               linux
               jamba1.5:large-fb99                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-dddb                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-07b2                    default  24G                 linux
               llama3.2:3b-instruct-15b2                    default  24G                 linux
               llama3.2:11b-vision-instruct-426b            default  80G                 linux
               llama3.2:90b-vision-instruct-4e67            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-7d94                   default  80Gx2               linux
llama4         llama4:17b-16e-scout-instruct-1da5           default  80Gx8               linux
               llama4:17b-128e-maverick-instruct-fp8-44a3   default  80Gx8               linux
mistral        mistral:8b-instruct-691e                     default  24G                 linux
               mistral:24b-small-instruct-2501-5244         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-ed8c        default  80Gx4               linux
phi4           phi4:14b-8fb6                                default  80G                 linux
pixtral        pixtral:12b-2409-5532                        default  80G                 linux
               pixtral:124b-2411-4480                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-8959                     default  24G                 linux
               qwen2.5:14b-instruct-5632                    default  80G                 linux
               qwen2.5:14b-instruct-awq-fcd4                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-62af          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-b404         default  24G                 linux
               qwen2.5:32b-instruct-a0f1                    default  80G                 linux
               qwen2.5:32b-instruct-awq-0b6b                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-37c3          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-72a5         default  40G                 linux
               qwen2.5:72b-instruct-52bd                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-bbb6                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-a7bc          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-b62f         default  80G                 linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-ccf5               default  24G                 linux
               qwen2.5-coder:7b-instruct-4e05               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-cf8c           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-9ae1     default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-1da1    default  24G                 linux
               qwen2.5-coder:14b-instruct-a6b7              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-1d72          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-8863    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-e75c   default  40G                 linux
               qwen2.5-coder:32b-instruct-5a11              default  80G                 linux
qwq            qwq:32b-b813                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.