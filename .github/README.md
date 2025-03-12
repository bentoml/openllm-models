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
deepseek       deepseek:r1-671b-08a3                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-b3e5         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-9179         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-919c         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-6f08        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-809e     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-a461    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-82f6    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-bc7c   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-4316   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-140c   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-cca5  default  80G                 linux
               deepseek:v3-671b-37b8                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-db9e                      default  12G                 linux
               gemma2:9b-instruct-6a69                      default  24G                 linux
               gemma2:27b-instruct-cf47                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-3622                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-bef1         default  80Gx6               linux
jamba1.5       jamba1.5:mini-5e51                           default  80Gx2               linux
               jamba1.5:large-1932                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-36e8                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-ca04                    default  24G                 linux
               llama3.2:3b-instruct-a691                    default  24G                 linux
               llama3.2:11b-vision-instruct-3a2b            default  80G                 linux
               llama3.2:90b-vision-instruct-1b16            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-3d21                   default  80Gx2               linux
mistral        mistral:8b-instruct-daa3                     default  24G                 linux
               mistral:24b-small-instruct-2501-e5bb         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-61c0        default  80Gx4               linux
phi4           phi4:14b-9128                                default  80G                 linux
pixtral        pixtral:12b-2409-9e60                        default  80G                 linux
               pixtral:124b-2411-c091                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-9155                     default  24G                 linux
               qwen2.5:14b-instruct-6099                    default  80G                 linux
               qwen2.5:14b-instruct-awq-ab20                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-8a8d          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-f3c5         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-910d     default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-4e26     default                      darwin
               qwen2.5:32b-instruct-71c7                    default  80G                 linux
               qwen2.5:32b-instruct-awq-e66f                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-db9e          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-bf96         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-7df9        default                      darwin
               qwen2.5:72b-instruct-4c9a                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-0883                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-ba06          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-050b         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-2ece     default                      darwin
qwen2.5-coder  qwen2.5-coder:3b-instruct-d2d9               default  24G                 linux
               qwen2.5-coder:7b-instruct-283f               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-e7b5           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-94c0     default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-d6c4    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-3eda    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-8a86   default                      darwin
               qwen2.5-coder:14b-instruct-ca85              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-7204          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-48fc    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-adfd   default  40G                 linux
               qwen2.5-coder:32b-instruct-ca7d              default  80G                 linux
qwq            qwq:32b-5b1b                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.