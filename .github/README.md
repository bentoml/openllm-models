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
deepseek       deepseek:r1-671b-6274                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-8dd1         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-dbee         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-ffba         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-63eb        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-0e9b     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-7c2e    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-0dc7    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-8c26   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-da90   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-347a   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-d784  default  80G                 linux
               deepseek:v3-671b-4c80                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-43f6                      default  12G                 linux
               gemma2:9b-instruct-ef95                      default  24G                 linux
               gemma2:27b-instruct-97f5                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-91e3                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-889d         default  80Gx6               linux
jamba1.5       jamba1.5:large-8b32                          default  80Gx8               linux
               jamba1.5:mini-a9e6                           default  80Gx2               linux
llama3.1       llama3.1:8b-instruct-0e43                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-a0b9                    default  24G                 linux
               llama3.2:3b-instruct-1fd4                    default  24G                 linux
               llama3.2:11b-vision-instruct-358f            default  80G                 linux
               llama3.2:90b-vision-instruct-5b10            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-502e                   default  80Gx2               linux
mistral        mistral:8b-instruct-0702                     default  24G                 linux
               mistral:24b-small-instruct-2501-10ee         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-1f1e        default  80Gx4               linux
phi4           phi4:14b-ef3f                                default  80G                 linux
pixtral        pixtral:12b-2409-2129                        default  80G                 linux
               pixtral:124b-2411-9567                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-5ff1                     default  24G                 linux
               qwen2.5:14b-instruct-3403                    default  80G                 linux
               qwen2.5:14b-instruct-awq-c3e9                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-1a66          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-62b6         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-49c9     default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-71fa     default                      darwin
               qwen2.5:32b-instruct-7a50                    default  80G                 linux
               qwen2.5:32b-instruct-awq-7228                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-4d65          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-abf5         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-db3e        default                      darwin
               qwen2.5:72b-instruct-7577                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-abd9                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-fc89          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-0dc0         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-52af     default                      darwin
qwen2.5-coder  qwen2.5-coder:3b-instruct-d0a8               default  24G                 linux
               qwen2.5-coder:7b-instruct-e5fd               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-214f           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-0d3d     default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-2dd0    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-aaa7    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-c71a   default                      darwin
               qwen2.5-coder:14b-instruct-84c6              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-2523          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-ca70    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-5cf9   default  40G                 linux
               qwen2.5-coder:32b-instruct-d578              default  80G                 linux
qwq            qwq:32b-9ce5                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.