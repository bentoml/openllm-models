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
deepseek       deepseek:r1-671b-32f8                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-d9aa         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-ce58         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-90f8         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-3c3d        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-eb43     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-1aeb    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-80b7    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-8d28   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-19c3   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-4dde   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-871c  default  80G                 linux
               deepseek:v3-671b-34bf                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-a1df                      default  12G                 linux
               gemma2:9b-instruct-eb87                      default  24G                 linux
               gemma2:27b-instruct-0df1                     default  80G                 linux
gemma3         gemma3:1b-instruct-2a1a                      default  12G                 linux
               gemma3:4b-instruct-82c8                      default  24G                 linux
               gemma3:12b-instruct-49c7                     default  40G                 linux
               gemma3:27b-instruct-4add                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-8cd5                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-0b07         default  80Gx8               linux
jamba1.5       jamba1.5:mini-ff0a                           default  80Gx2               linux
               jamba1.5:large-f40c                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-895c                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-e938                    default  24G                 linux
               llama3.2:3b-instruct-a294                    default  24G                 linux
               llama3.2:11b-vision-instruct-8a24            default  80G                 linux
               llama3.2:90b-vision-instruct-1089            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-396d                   default  80Gx2               linux
llama4         llama4:17b-16e-scout-instruct-22b6           default  80Gx8               linux
               llama4:17b-128e-maverick-instruct-fp8-a39d   default  80Gx8               linux
mistral        mistral:8b-instruct-bb93                     default  24G                 linux
               mistral:24b-small-instruct-2501-00d4         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-4849        default  80Gx4               linux
phi4           phi4:14b-4804                                default  80G                 linux
pixtral        pixtral:12b-2409-5fba                        default  80G                 linux
               pixtral:124b-2411-48eb                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-04fa                     default  24G                 linux
               qwen2.5:14b-instruct-03fa                    default  80G                 linux
               qwen2.5:14b-instruct-awq-642b                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-3cd5          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-4f49         default  24G                 linux
               qwen2.5:32b-instruct-b5c5                    default  80G                 linux
               qwen2.5:32b-instruct-awq-0612                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-e87e          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-0e83         default  40G                 linux
               qwen2.5:72b-instruct-4f02                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-2274                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-2c47          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-11d9         default  80G                 linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-81b3               default  24G                 linux
               qwen2.5-coder:7b-instruct-db8c               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-776c           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-2bc8     default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-d3c4    default  24G                 linux
               qwen2.5-coder:14b-instruct-867e              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-cd43          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-2f1a    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-64fe   default  40G                 linux
               qwen2.5-coder:32b-instruct-955f              default  80G                 linux
qwq            qwq:32b-37c8                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.