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
deepseek       deepseek:r1-671b-229e                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-999b         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-77bb         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-7c7c         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-a3fb        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-08ed     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-a201    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-a50e    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-f6b9   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-9885   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-e695   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-a226  default  80G                 linux
               deepseek:v3-671b-2047                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-17f2                      default  12G                 linux
               gemma2:9b-instruct-347f                      default  24G                 linux
               gemma2:27b-instruct-205c                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-775a                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-37d1         default  80Gx6               linux
jamba1.5       jamba1.5:large-38b3                          default  80Gx8               linux
               jamba1.5:mini-73d5                           default  80Gx2               linux
llama3.1       llama3.1:8b-instruct-46ea                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-1836                    default  24G                 linux
               llama3.2:3b-instruct-784e                    default  24G                 linux
               llama3.2:11b-vision-instruct-1639            default  80G                 linux
               llama3.2:90b-vision-instruct-3fa6            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-e1c5                   default  80Gx2               linux
mistral        mistral:8b-instruct-b290                     default  24G                 linux
               mistral:24b-small-instruct-2501-9925         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-5cca        default  80Gx4               linux
phi4           phi4:14b-3c21                                default  80G                 linux
pixtral        pixtral:12b-2409-07ac                        default  80G                 linux
               pixtral:124b-2411-d6c7                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-82f2                     default  24G                 linux
               qwen2.5:14b-instruct-e151                    default  80G                 linux
               qwen2.5:14b-instruct-awq-08a6                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-79d8          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-79d8         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-910d     default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-4e26     default                      darwin
               qwen2.5:32b-instruct-82dc                    default  80G                 linux
               qwen2.5:32b-instruct-awq-9a7f                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-9028          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-b6d9         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-7df9        default                      darwin
               qwen2.5:72b-instruct-96ac                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-4253                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-d782          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-f139         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-2ece     default                      darwin
qwen2.5-coder  qwen2.5-coder:3b-instruct-7bfc               default  24G                 linux
               qwen2.5-coder:7b-instruct-da5f               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-396d           default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-d6c4    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-7cc8    default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a16-292d    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-8a86   default                      darwin
               qwen2.5-coder:14b-instruct-61dd              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-1b4f          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-9a6f    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-b2f8   default  40G                 linux
               qwen2.5-coder:32b-instruct-963c              default  80G                 linux
qwq            qwq:32b-3551                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.