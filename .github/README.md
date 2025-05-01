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
deepseek       deepseek:r1-671b-d485                        default  141Gx8              linux
               deepseek:r1-distill-llama3.1-8b-d683         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-26db         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-b3e6         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-2dd7        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-af5d     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-6bdd    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-8029    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-275a   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-79af   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-4532   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-dd79  default  80G                 linux
               deepseek:prover-v2-671b-f7ad                 default  141Gx8              linux
               deepseek:v3-671b-4db7                        default  141Gx8              linux
gemma2         gemma2:2b-instruct-4479                      default  12G                 linux
               gemma2:9b-instruct-7899                      default  24G                 linux
               gemma2:27b-instruct-95fb                     default  80G                 linux
gemma3         gemma3:1b-instruct-01d6                      default  12G                 linux
               gemma3:4b-instruct-5620                      default  24G                 linux
               gemma3:12b-instruct-d4e0                     default  40G                 linux
               gemma3:27b-instruct-a9ba                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-248e                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-2bb5         default  80Gx8               linux
jamba1.5       jamba1.5:large-d82e                          default  80Gx8               linux
               jamba1.5:mini-0357                           default  80Gx2               linux
llama3.1       llama3.1:8b-instruct-239c                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-c665                    default  24G                 linux
               llama3.2:3b-instruct-d883                    default  24G                 linux
               llama3.2:11b-vision-instruct-f457            default  80G                 linux
               llama3.2:90b-vision-instruct-9d8b            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-c968                   default  80Gx2               linux
llama4         llama4:17b-16e-scout-instruct-73f7           default  80Gx8               linux
               llama4:17b-128e-maverick-instruct-fp8-a264   default  80Gx8               linux
mistral        mistral:8b-instruct-983c                     default  24G                 linux
               mistral:24b-small-instruct-2501-4045         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-4221        default  80Gx4               linux
phi4           phi4:14b-5f46                                default  80G                 linux
pixtral        pixtral:12b-2409-0e0a                        default  80G                 linux
               pixtral:124b-2411-4f09                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-fefe                     default  24G                 linux
               qwen2.5:14b-instruct-6f05                    default  80G                 linux
               qwen2.5:14b-instruct-awq-dee2                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-ae1a          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-7158         default  24G                 linux
               qwen2.5:32b-instruct-2dd5                    default  80G                 linux
               qwen2.5:32b-instruct-awq-84cd                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-9ab1          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-de25         default  40G                 linux
               qwen2.5:72b-instruct-1ce1                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-44d2                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-ed2c          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-c653         default  80G                 linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-6dd3               default  24G                 linux
               qwen2.5-coder:7b-instruct-92ec               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-6bab           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-4007     default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-b095    default  24G                 linux
               qwen2.5-coder:14b-instruct-e540              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-1882          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-2b56    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-238e   default  40G                 linux
               qwen2.5-coder:32b-instruct-8d05              default  80G                 linux
qwen3          qwen3:8b-2033                                default  24G                 linux
               qwen3:30b-a3b-6b9d                           default  80Gx2               linux
               qwen3:235b-a22b-fp8-1a79                     default  80Gx4               linux
qwq            qwq:32b-1c08                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.