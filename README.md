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
deepseek       deepseek:r1-671b-eb32                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-626a         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-3728         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-63b0         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-4b47        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-2ca1     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-4603    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-9ce2    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-31b4   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-0e8a   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-ca5e   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-18c2  default  80G                 linux
               deepseek:v3-671b-2e40                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-868c                      default  12G                 linux
               gemma2:9b-instruct-e44c                      default  24G                 linux
               gemma2:27b-instruct-3826                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-1242                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-24ff         default  80Gx6               linux
jamba1.5       jamba1.5:mini-4f7f                           default  80Gx2               linux
               jamba1.5:large-e809                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-a995                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-6fa1                    default  24G                 linux
               llama3.2:3b-instruct-7d96                    default  24G                 linux
               llama3.2:11b-vision-instruct-eac2            default  80G                 linux
               llama3.2:90b-vision-instruct-25ca            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-f791                   default  80Gx2               linux
mistral        mistral:8b-instruct-f4ed                     default  24G                 linux
               mistral:24b-small-instruct-2501-cc81         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-e1ef        default  80Gx4               linux
phi4           phi4:14b-a515                                default  80G                 linux
pixtral        pixtral:12b-2409-a2e0                        default  80G                 linux
               pixtral:124b-2411-9886                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-dbe1                     default  24G                 linux
               qwen2.5:14b-instruct-d1f8                    default  80G                 linux
               qwen2.5:14b-instruct-awq-59be                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-fa83          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-fa83         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-009a     default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-add0     default                      darwin
               qwen2.5:32b-instruct-e0dc                    default  80G                 linux
               qwen2.5:32b-instruct-awq-0fcd                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-a809          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-66e8         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-75c6        default                      darwin
               qwen2.5:72b-instruct-8557                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-36de                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-e038          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-b0c5         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-2a15     default                      darwin
qwen2.5-coder  qwen2.5-coder:3b-instruct-63b0               default  24G                 linux
               qwen2.5-coder:7b-instruct-a819               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-63c9           default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-d531    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-dfcf    default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a16-1ff4    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-33fb   default                      darwin
               qwen2.5-coder:14b-instruct-e2e9              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-5456          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-0910    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-d2dc   default  40G                 linux
               qwen2.5-coder:32b-instruct-1950              default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.