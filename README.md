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
deepseek       deepseek:r1-671b-8b50                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-b4fd         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-0dc4         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-f94b         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-3b5a        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-c73b     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-4f0b    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-2102    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-aa04   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-a615   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-53da   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-6d9e  default  80G                 linux
               deepseek:v3-671b-f10f                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-e7b8                      default  12G                 linux
               gemma2:9b-instruct-8cfb                      default  24G                 linux
               gemma2:27b-instruct-dabb                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-cbb3                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-8f4b         default  80Gx6               linux
jamba1.5       jamba1.5:large-4c0b                          default  80Gx8               linux
               jamba1.5:mini-22d6                           default  80Gx2               linux
llama3.1       llama3.1:8b-instruct-abad                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-d787                    default  24G                 linux
               llama3.2:3b-instruct-bb1f                    default  24G                 linux
               llama3.2:11b-vision-instruct-d189            default  80G                 linux
               llama3.2:90b-vision-instruct-8f7a            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-496b                   default  80Gx2               linux
mistral        mistral:8b-instruct-2b9e                     default  24G                 linux
               mistral:24b-small-instruct-2501-daeb         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-ce45        default  80Gx4               linux
phi4           phi4:14b-66fa                                default  80G                 linux
pixtral        pixtral:12b-2409-1def                        default  80G                 linux
               pixtral:124b-2411-4345                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-de0d                     default  24G                 linux
               qwen2.5:14b-instruct-b331                    default  80G                 linux
               qwen2.5:14b-instruct-awq-2162                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-0393          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-0393         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-904c     default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-c127     default                      darwin
               qwen2.5:32b-instruct-fb62                    default  80G                 linux
               qwen2.5:32b-instruct-awq-835d                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-1949          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-3bed         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-5136        default                      darwin
               qwen2.5:72b-instruct-fbb8                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-cb6c                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-45f9          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-5410         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-d900     default                      darwin
qwen2.5-coder  qwen2.5-coder:3b-instruct-44b4               default  24G                 linux
               qwen2.5-coder:7b-instruct-9d06               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-92e2           default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-497b    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-98fa    default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a16-7fd3    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-2938   default                      darwin
               qwen2.5-coder:14b-instruct-73ef              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-db22          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-e7df    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-55df   default  40G                 linux
               qwen2.5-coder:32b-instruct-dd35              default  80G                 linux
qwq            qwq:32b-d8aa                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.