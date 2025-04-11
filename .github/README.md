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
deepseek       deepseek:r1-671b-034e                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-918e         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-4cb9         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-91c8         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-8fdd        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-a83b     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-d3c1    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-c71d    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-b6c9   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-0597   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-c6a1   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-cbca  default  80G                 linux
               deepseek:v3-671b-74c6                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-d06a                      default  12G                 linux
               gemma2:9b-instruct-ac58                      default  24G                 linux
               gemma2:27b-instruct-51f9                     default  80G                 linux
gemma3         gemma3:1b-instruct-46dd                      default  12G                 linux
               gemma3:4b-instruct-8bbc                      default  24G                 linux
               gemma3:12b-instruct-e89f                     default  40G                 linux
               gemma3:27b-instruct-b20a                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-c6d7                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-b4d8         default  80Gx8               linux
jamba1.5       jamba1.5:mini-5aa5                           default  80Gx2               linux
               jamba1.5:large-dc41                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-ef2e                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-076d                    default  24G                 linux
               llama3.2:3b-instruct-5db6                    default  24G                 linux
               llama3.2:11b-vision-instruct-a3b8            default  80G                 linux
               llama3.2:90b-vision-instruct-6a91            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-433b                   default  80Gx2               linux
llama4         llama4:17b-16e-scout-instruct-84c3           default  80Gx8               linux
               llama4:17b-128e-maverick-instruct-fp8-cf64   default  80Gx8               linux
mistral        mistral:8b-instruct-87ff                     default  24G                 linux
               mistral:24b-small-instruct-2501-d6e3         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-809a        default  80Gx4               linux
phi4           phi4:14b-1b68                                default  80G                 linux
pixtral        pixtral:12b-2409-05e3                        default  80G                 linux
               pixtral:124b-2411-a0db                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-6344                     default  24G                 linux
               qwen2.5:14b-instruct-9033                    default  80G                 linux
               qwen2.5:14b-instruct-awq-a2af                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-f58a          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-b049         default  24G                 linux
               qwen2.5:32b-instruct-3529                    default  80G                 linux
               qwen2.5:32b-instruct-awq-15e0                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-0273          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-db96         default  40G                 linux
               qwen2.5:72b-instruct-86a3                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-215d                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-baa4          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-783a         default  80G                 linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-82c0               default  24G                 linux
               qwen2.5-coder:7b-instruct-12e1               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-f5b8           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-4a26     default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-3158    default  24G                 linux
               qwen2.5-coder:14b-instruct-d6ed              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-b85e          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-a62c    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-4804   default  40G                 linux
               qwen2.5-coder:32b-instruct-ce0a              default  80G                 linux
qwq            qwq:32b-634e                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.