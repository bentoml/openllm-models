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
deepseek       deepseek:r1-671b-1328                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-5e6b         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-e937         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-aff6         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-f7db        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-c308     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-d322    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-8d52    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-6ce6   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-3c9f   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-c3e5   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-58b8  default  80G                 linux
               deepseek:v3-671b-8f3e                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-3e96                      default  12G                 linux
               gemma2:9b-instruct-0648                      default  24G                 linux
               gemma2:27b-instruct-d14e                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-e691                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-e7cb         default  80Gx6               linux
jamba1.5       jamba1.5:mini-339e                           default  80Gx2               linux
               jamba1.5:large-5651                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-3c13                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-ec57                    default  24G                 linux
               llama3.2:3b-instruct-b266                    default  24G                 linux
               llama3.2:11b-vision-instruct-b57b            default  80G                 linux
               llama3.2:90b-vision-instruct-b548            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-e93f                   default  80Gx2               linux
mistral        mistral:8b-instruct-42d3                     default  24G                 linux
               mistral:24b-small-instruct-2501-80ed         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-099a        default  80Gx4               linux
phi4           phi4:14b-7fce                                default  80G                 linux
pixtral        pixtral:12b-2409-d90f                        default  80G                 linux
               pixtral:124b-2411-4267                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-670e                     default  24G                 linux
               qwen2.5:14b-instruct-fddf                    default  80G                 linux
               qwen2.5:14b-instruct-awq-27c0                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-2a3d          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-1541         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-910d     default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-4e26     default                      darwin
               qwen2.5:32b-instruct-2e17                    default  80G                 linux
               qwen2.5:32b-instruct-awq-fea8                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-cef0          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-f303         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-7df9        default                      darwin
               qwen2.5:72b-instruct-69da                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-9d24                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-3a79          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-b40f         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-2ece     default                      darwin
qwen2.5-coder  qwen2.5-coder:3b-instruct-5bbe               default  24G                 linux
               qwen2.5-coder:7b-instruct-2737               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-dc1b           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-b5a7     default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-d6c4    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-1bef    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-8a86   default                      darwin
               qwen2.5-coder:14b-instruct-8170              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-a1f7          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-3d02    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-2cc6   default  40G                 linux
               qwen2.5-coder:32b-instruct-c208              default  80G                 linux
qwq            qwq:32b-e98e                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.