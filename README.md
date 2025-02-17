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
deepseek       deepseek:r1-671b-c498                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-f814         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-f937         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-bbb7         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-ca58        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-8441     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-114f    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-a633    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-a4cc   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-17b1   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-accc   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-14c6  default  80G                 linux
               deepseek:v3-671b-ad20                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-422a                      default  12G                 linux
               gemma2:9b-instruct-a502                      default  24G                 linux
               gemma2:27b-instruct-15c5                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-6648                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-e3e4         default  80Gx6               linux
jamba1.5       jamba1.5:mini-ba7a                           default  80Gx2               linux
               jamba1.5:large-4770                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-7364                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-5578                    default  24G                 linux
               llama3.2:3b-instruct-2357                    default  24G                 linux
               llama3.2:11b-vision-instruct-e7cf            default  80G                 linux
               llama3.2:90b-vision-instruct-8c04            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-6242                   default  80Gx2               linux
mistral        mistral:8b-instruct-7876                     default  24G                 linux
               mistral:24b-small-instruct-2501-a098         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-811d        default  80Gx4               linux
phi4           phi4:14b-eff8                                default  80G                 linux
pixtral        pixtral:12b-2409-32d5                        default  80G                 linux
               pixtral:124b-2411-2094                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-8272                     default  24G                 linux
               qwen2.5:14b-instruct-4c22                    default  80G                 linux
               qwen2.5:14b-instruct-awq-54be                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-0031          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-0031         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-c031     default                      linux
               qwen2.5:14b-instruct-ggml-q8-darwin-460d     default                      linux
               qwen2.5:32b-instruct-fc84                    default  80G                 linux
               qwen2.5:32b-instruct-awq-e91b                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-531c          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-ebc6         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-dc51        default                      linux
               qwen2.5:72b-instruct-a284                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-c25b                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-7177          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-7c7a         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-7318     default                      linux
qwen2.5-coder  qwen2.5-coder:3b-instruct-8f52               default  24G                 linux
               qwen2.5-coder:7b-instruct-8959               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-96ce           default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-7626    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-de7a    default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a16-9b94    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-8afd   default                      linux
               qwen2.5-coder:14b-instruct-4c1f              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-66f2          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-a4ef    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-46aa   default  40G                 linux
               qwen2.5-coder:32b-instruct-af5b              default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.