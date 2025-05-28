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
deepseek       deepseek:r1-671b-d88a                        default  141Gx8              linux
               deepseek:r1-distill-llama3.1-8b-ef0f         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-bfa1         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-f45f         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-8ee6        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-8895     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-2cf9    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-7c45    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-ae4b   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-961f   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-04dd   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-fb66  default  80G                 linux
               deepseek:prover-v2-671b-1bf4                 default  141Gx8              linux
               deepseek:v3-671b-3649                        default  141Gx8              linux
gemma2         gemma2:2b-instruct-02c5                      default  12G                 linux
               gemma2:9b-instruct-4fef                      default  24G                 linux
               gemma2:27b-instruct-4536                     default  80G                 linux
gemma3         gemma3:1b-instruct-ab73                      default  12G                 linux
               gemma3:4b-instruct-fb2c                      default  24G                 linux
               gemma3:12b-instruct-0f67                     default  40G                 linux
               gemma3:27b-instruct-aa27                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-12ff                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-139b         default  80Gx8               linux
jamba1.5       jamba1.5:large-4cd5                          default  80Gx8               linux
               jamba1.5:mini-e9f8                           default  80Gx2               linux
llama3.1       llama3.1:8b-instruct-b6a9                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-b1f5                    default  24G                 linux
               llama3.2:3b-instruct-d936                    default  24G                 linux
               llama3.2:11b-vision-instruct-b9e6            default  80G                 linux
               llama3.2:90b-vision-instruct-aaac            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-77ee                   default  80Gx2               linux
llama4         llama4:17b-16e-scout-instruct-6074           default  80Gx8               linux
               llama4:17b-128e-maverick-instruct-fp8-41e2   default  80Gx8               linux
mistral        mistral:8b-instruct-395a                     default  24G                 linux
               mistral:24b-small-instruct-2501-c169         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-069b        default  80Gx4               linux
phi4           phi4:14b-26c7                                default  80G                 linux
pixtral        pixtral:12b-2409-ddd5                        default  80G                 linux
               pixtral:124b-2411-835d                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-8b6c                     default  24G                 linux
               qwen2.5:14b-instruct-07fe                    default  80G                 linux
               qwen2.5:14b-instruct-awq-2bdf                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-79fb          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-232a         default  24G                 linux
               qwen2.5:32b-instruct-fe34                    default  80G                 linux
               qwen2.5:32b-instruct-awq-e81c                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-324c          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-f044         default  40G                 linux
               qwen2.5:72b-instruct-9995                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-1722                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-59a8          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-8f64         default  80G                 linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-a61d               default  24G                 linux
               qwen2.5-coder:7b-instruct-8240               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-b6f3           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-a5c5     default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-8a64    default  24G                 linux
               qwen2.5-coder:14b-instruct-e11b              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-67ae          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-5927    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-4695   default  40G                 linux
               qwen2.5-coder:32b-instruct-d3cd              default  80G                 linux
qwen3          qwen3:8b-cb10                                default  24G                 linux
               qwen3:30b-a3b-47c4                           default  80Gx2               linux
               qwen3:235b-a22b-fp8-f383                     default  80Gx4               linux
qwq            qwq:32b-a2ca                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.