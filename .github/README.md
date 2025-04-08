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
deepseek       deepseek:r1-671b-1c34                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-e91a         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-0b2a         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-4040         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-ff4e        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-95ae     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-d494    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-3143    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-bbdc   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-fea1   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-c9cb   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-9b77  default  80G                 linux
               deepseek:v3-671b-492c                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-5ca6                      default  12G                 linux
               gemma2:9b-instruct-34de                      default  24G                 linux
               gemma2:27b-instruct-b2be                     default  80G                 linux
gemma3         gemma3:1b-instruct-15d1                      default  12G                 linux
               gemma3:4b-instruct-bec9                      default  24G                 linux
               gemma3:12b-instruct-489d                     default  40G                 linux
               gemma3:27b-instruct-6bf3                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-0ca6                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-6e74         default  80Gx6               linux
jamba1.5       jamba1.5:mini-119f                           default  80Gx2               linux
               jamba1.5:large-183b                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-6a85                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-e929                    default  24G                 linux
               llama3.2:3b-instruct-2d54                    default  24G                 linux
               llama3.2:11b-vision-instruct-e0d9            default  80G                 linux
               llama3.2:90b-vision-instruct-3c95            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-7931                   default  80Gx2               linux
llama4         llama4:17b-16e-scout-instruct-eefd           default  80Gx2               linux
               llama4:17b-128e-maverick-instruct-1125       default  80Gx8               linux
mistral        mistral:8b-instruct-24da                     default  24G                 linux
               mistral:24b-small-instruct-2501-9670         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-595e        default  80Gx4               linux
phi4           phi4:14b-ab88                                default  80G                 linux
pixtral        pixtral:12b-2409-c898                        default  80G                 linux
               pixtral:124b-2411-8f41                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-dd4f                     default  24G                 linux
               qwen2.5:14b-instruct-b9c4                    default  80G                 linux
               qwen2.5:14b-instruct-awq-2328                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-b779          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-daed         default  24G                 linux
               qwen2.5:32b-instruct-cd3f                    default  80G                 linux
               qwen2.5:32b-instruct-awq-94c3                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-e644          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-e14a         default  40G                 linux
               qwen2.5:72b-instruct-84cf                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-2360                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-3b21          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-c162         default  80G                 linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-8a1a               default  24G                 linux
               qwen2.5-coder:7b-instruct-bdee               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-5fc5           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-81fc     default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-c38d    default  24G                 linux
               qwen2.5-coder:14b-instruct-5aea              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-cf8a          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-036b    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-990a   default  40G                 linux
               qwen2.5-coder:32b-instruct-8a0c              default  80G                 linux
qwq            qwq:32b-c54b                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.