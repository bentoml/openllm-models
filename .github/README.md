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
deepseek       deepseek:r1-671b-ce12                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-a5d8         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-8aed         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-fa33         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-2191        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-13f2     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-8457    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-7253    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-3d56   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-7244   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-a8b1   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-d111  default  80G                 linux
               deepseek:v3-671b-bd36                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-bf05                      default  12G                 linux
               gemma2:9b-instruct-2374                      default  24G                 linux
               gemma2:27b-instruct-ebaa                     default  80G                 linux
gemma3         gemma3:1b-instruct-18c0                      default  12G                 linux
               gemma3:4b-instruct-5986                      default  24G                 linux
               gemma3:12b-instruct-a9f9                     default  40G                 linux
               gemma3:27b-instruct-5796                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-3e02                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-f9c6         default  80Gx8               linux
jamba1.5       jamba1.5:mini-f29a                           default  80Gx2               linux
               jamba1.5:large-77cd                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-7d76                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-28da                    default  24G                 linux
               llama3.2:3b-instruct-23ab                    default  24G                 linux
               llama3.2:11b-vision-instruct-a840            default  80G                 linux
               llama3.2:90b-vision-instruct-c3f2            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-5845                   default  80Gx2               linux
llama4         llama4:17b-16e-scout-instruct-a988           default  80Gx8               linux
               llama4:17b-128e-maverick-instruct-fp8-c62f   default  80Gx8               linux
mistral        mistral:8b-instruct-c0ae                     default  24G                 linux
               mistral:24b-small-instruct-2501-704c         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-8dbf        default  80Gx4               linux
phi4           phi4:14b-db84                                default  80G                 linux
pixtral        pixtral:12b-2409-cee4                        default  80G                 linux
               pixtral:124b-2411-1898                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-d412                     default  24G                 linux
               qwen2.5:14b-instruct-f674                    default  80G                 linux
               qwen2.5:14b-instruct-awq-f6e4                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-f316          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-f0df         default  24G                 linux
               qwen2.5:32b-instruct-34bc                    default  80G                 linux
               qwen2.5:32b-instruct-awq-eff5                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-1316          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-21b6         default  40G                 linux
               qwen2.5:72b-instruct-db5a                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-4d12                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-adf9          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-c5d7         default  80G                 linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-0898               default  24G                 linux
               qwen2.5-coder:7b-instruct-dab4               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-8991           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-e980     default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-646e    default  24G                 linux
               qwen2.5-coder:14b-instruct-a3fc              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-8051          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-08c9    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-e9c3   default  40G                 linux
               qwen2.5-coder:32b-instruct-2dba              default  80G                 linux
qwq            qwq:32b-35dc                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.