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
deepseek       deepseek:r1-671b-3936                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-17ac         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-3fde         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-ab4f         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-2a19        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-2b54     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-52ec    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-fbd2    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-7248   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-5335   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-764e   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-a076  default  80G                 linux
               deepseek:v3-671b-090c                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-5ebf                      default  12G                 linux
               gemma2:9b-instruct-c46b                      default  24G                 linux
               gemma2:27b-instruct-399d                     default  80G                 linux
gemma3         gemma3:1b-instruct-53b6                      default  12G                 linux
               gemma3:4b-instruct-0b56                      default  24G                 linux
               gemma3:12b-instruct-c598                     default  40G                 linux
               gemma3:27b-instruct-36c4                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-d39a                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-0b3b         default  80Gx8               linux
jamba1.5       jamba1.5:mini-5076                           default  80Gx2               linux
               jamba1.5:large-7350                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-f4ac                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-071f                    default  24G                 linux
               llama3.2:3b-instruct-cbd4                    default  24G                 linux
               llama3.2:11b-vision-instruct-2fab            default  80G                 linux
               llama3.2:90b-vision-instruct-882c            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-c914                   default  80Gx2               linux
llama4         llama4:17b-16e-scout-instruct-60e2           default  80Gx8               linux
               llama4:17b-128e-maverick-instruct-fp8-2960   default  80Gx8               linux
mistral        mistral:8b-instruct-ce45                     default  24G                 linux
               mistral:24b-small-instruct-2501-0b70         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-b5b6        default  80Gx4               linux
phi4           phi4:14b-110f                                default  80G                 linux
pixtral        pixtral:12b-2409-595c                        default  80G                 linux
               pixtral:124b-2411-6d46                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-525f                     default  24G                 linux
               qwen2.5:14b-instruct-600b                    default  80G                 linux
               qwen2.5:14b-instruct-awq-36f0                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-e5c9          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-ba4f         default  24G                 linux
               qwen2.5:32b-instruct-2c99                    default  80G                 linux
               qwen2.5:32b-instruct-awq-f1b6                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-0e59          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-e432         default  40G                 linux
               qwen2.5:72b-instruct-4aa9                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-a60a                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-c89b          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-c951         default  80G                 linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-9135               default  24G                 linux
               qwen2.5-coder:7b-instruct-e653               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-aa24           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-8dcb     default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-c518    default  24G                 linux
               qwen2.5-coder:14b-instruct-20f5              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-7ef4          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-1502    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-ef10   default  40G                 linux
               qwen2.5-coder:32b-instruct-57b7              default  80G                 linux
qwen3          qwen3:8b-instruct-4a9b                       default  24G                 linux
               qwen3:235b-a22b-fp8-81d3                     default  80Gx4               linux
qwq            qwq:32b-5488                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.