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
deepseek       deepseek:r1-671b-548c                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-98f8         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-a92e         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-7e19         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-0f10        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-d6b8     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-7b36    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-47d7    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-4dd3   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-abc8   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-1528   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-db03  default  80G                 linux
               deepseek:v3-671b-255a                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-7d49                      default  12G                 linux
               gemma2:9b-instruct-9a79                      default  24G                 linux
               gemma2:27b-instruct-8e04                     default  80G                 linux
gemma3         gemma3:1b-instruct-e94b                      default  12G                 linux
               gemma3:4b-instruct-9de8                      default  24G                 linux
               gemma3:12b-instruct-f4d4                     default  40G                 linux
               gemma3:27b-instruct-d277                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-5243                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-396f         default  80Gx6               linux
jamba1.5       jamba1.5:mini-96c2                           default  80Gx2               linux
               jamba1.5:large-e401                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-c2b5                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-1852                    default  24G                 linux
               llama3.2:3b-instruct-bf83                    default  24G                 linux
               llama3.2:11b-vision-instruct-9ecf            default  80G                 linux
               llama3.2:90b-vision-instruct-6fb7            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-218b                   default  80Gx2               linux
llama4         llama4:17b-16e-scout-instruct-b6e9           default  80Gx2               linux
               llama4:17b-128e-maverick-instruct-dc4b       default  80Gx8               linux
mistral        mistral:8b-instruct-511e                     default  24G                 linux
               mistral:24b-small-instruct-2501-f76f         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-b02e        default  80Gx4               linux
phi4           phi4:14b-f33b                                default  80G                 linux
pixtral        pixtral:12b-2409-3fcf                        default  80G                 linux
               pixtral:124b-2411-d6e3                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-d01a                     default  24G                 linux
               qwen2.5:14b-instruct-f0a3                    default  80G                 linux
               qwen2.5:14b-instruct-awq-04fb                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-9e13          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-201a         default  24G                 linux
               qwen2.5:32b-instruct-2585                    default  80G                 linux
               qwen2.5:32b-instruct-awq-44ef                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-c1bc          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-8ba4         default  40G                 linux
               qwen2.5:72b-instruct-f3d9                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-045f                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-f45e          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-e581         default  80G                 linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-199b               default  24G                 linux
               qwen2.5-coder:7b-instruct-25de               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-788b           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-27a8     default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-9d7b    default  24G                 linux
               qwen2.5-coder:14b-instruct-20d8              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-83df          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-45c8    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-8019   default  40G                 linux
               qwen2.5-coder:32b-instruct-f878              default  80G                 linux
qwq            qwq:32b-d776                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.