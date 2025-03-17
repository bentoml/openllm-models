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
deepseek       deepseek:r1-671b-339c                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-c0a0         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-197f         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-a59f         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-d43a        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-9bd3     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-f632    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-c0a8    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-2491   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-28f7   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-3dd3   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-dfc1  default  80G                 linux
               deepseek:v3-671b-490d                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-943f                      default  12G                 linux
               gemma2:9b-instruct-be25                      default  24G                 linux
               gemma2:27b-instruct-787e                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-5316                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-1722         default  80Gx6               linux
jamba1.5       jamba1.5:large-4696                          default  80Gx8               linux
               jamba1.5:mini-9806                           default  80Gx2               linux
llama3.1       llama3.1:8b-instruct-7376                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-99ea                    default  24G                 linux
               llama3.2:3b-instruct-c06c                    default  24G                 linux
               llama3.2:11b-vision-instruct-710d            default  80G                 linux
               llama3.2:90b-vision-instruct-0795            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-d28c                   default  80Gx2               linux
mistral        mistral:8b-instruct-4c4c                     default  24G                 linux
               mistral:24b-small-instruct-2501-2e10         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-ef11        default  80Gx4               linux
phi4           phi4:14b-49cd                                default  80G                 linux
pixtral        pixtral:12b-2409-fa6a                        default  80G                 linux
               pixtral:124b-2411-d4a9                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-3b8b                     default  24G                 linux
               qwen2.5:14b-instruct-2bbd                    default  80G                 linux
               qwen2.5:14b-instruct-awq-d922                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-ca41          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-040c         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-49c9     default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-71fa     default                      darwin
               qwen2.5:32b-instruct-6ca6                    default  80G                 linux
               qwen2.5:32b-instruct-awq-e88f                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-94d5          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-27ba         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-db3e        default                      darwin
               qwen2.5:72b-instruct-eb02                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-c0e5                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-c430          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-0b94         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-52af     default                      darwin
qwen2.5-coder  qwen2.5-coder:3b-instruct-9554               default  24G                 linux
               qwen2.5-coder:7b-instruct-ea9b               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-3066           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-435e     default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-2dd0    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-967a    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-c71a   default                      darwin
               qwen2.5-coder:14b-instruct-7372              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-7fe8          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-609c    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-3bd1   default  40G                 linux
               qwen2.5-coder:32b-instruct-fe2f              default  80G                 linux
qwq            qwq:32b-95df                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.