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
deepseek       deepseek:r1-671b-0062                        default  80Gx16              linux
               deepseek:r1-distill-llama3.1-8b-e857         default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-0d3f         default  80G                 linux
               deepseek:r1-distill-qwen2.5-32b-5242         default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-d0d6        default  80Gx2               linux
               deepseek:r1-distill-qwen2.5-7b-math-2d07     default  24G                 linux
               deepseek:r1-distill-qwen2.5-14b-w8a8-bab1    default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w8a8-e4f6    default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w8a8-af86   default  80G                 linux
               deepseek:r1-distill-qwen2.5-14b-w4a16-45a2   default  24G                 linux
               deepseek:r1-distill-qwen2.5-32b-w4a16-ad6f   default  80G                 linux
               deepseek:r1-distill-llama3.3-70b-w4a16-01a9  default  80G                 linux
               deepseek:v3-671b-15b7                        default  80Gx16              linux
gemma2         gemma2:2b-instruct-ab01                      default  12G                 linux
               gemma2:9b-instruct-beb2                      default  24G                 linux
               gemma2:27b-instruct-1a99                     default  80G                 linux
gemma3         gemma3:1b-instruct-666e                      default  12G                 linux
               gemma3:4b-instruct-df97                      default  24G                 linux
               gemma3:12b-instruct-71e7                     default  40G                 linux
               gemma3:27b-instruct-daed                     default  80G                 linux
hermes-3       hermes-3:deep-llama3-8b-3d2c                 default  80G                 linux
               hermes-3:llama3.1-405b-instruct-6625         default  80Gx6               linux
jamba1.5       jamba1.5:mini-64a8                           default  80Gx2               linux
               jamba1.5:large-0396                          default  80Gx8               linux
llama3.1       llama3.1:8b-instruct-1791                    default  24G                 linux
llama3.2       llama3.2:1b-instruct-fbb1                    default  24G                 linux
               llama3.2:3b-instruct-7359                    default  24G                 linux
               llama3.2:11b-vision-instruct-a0c2            default  80G                 linux
               llama3.2:90b-vision-instruct-0135            default  80Gx2               linux
llama3.3       llama3.3:70b-instruct-7407                   default  80Gx2               linux
mistral        mistral:8b-instruct-8074                     default  24G                 linux
               mistral:24b-small-instruct-2501-1168         default  80G                 linux
mistral-large  mistral-large:123b-instruct-2407-669d        default  80Gx4               linux
phi4           phi4:14b-e5be                                default  80G                 linux
pixtral        pixtral:12b-2409-74f1                        default  80G                 linux
               pixtral:124b-2411-a4ee                       default  80Gx4               linux
qwen2.5        qwen2.5:7b-instruct-b0ba                     default  24G                 linux
               qwen2.5:14b-instruct-5580                    default  80G                 linux
               qwen2.5:14b-instruct-awq-a841                default  24G                 linux
               qwen2.5:14b-instruct-gptq-w8a8-c70c          default  24G                 linux
               qwen2.5:14b-instruct-gptq-w4a16-5775         default  24G                 linux
               qwen2.5:14b-instruct-ggml-q4-darwin-e7a8     default                      darwin
               qwen2.5:14b-instruct-ggml-q8-darwin-4db7     default                      darwin
               qwen2.5:32b-instruct-38b1                    default  80G                 linux
               qwen2.5:32b-instruct-awq-d9c1                default  40G                 linux
               qwen2.5:32b-instruct-gptq-w8a8-e53c          default  40G                 linux
               qwen2.5:32b-instruct-gptq-w4a16-6d6e         default  40G                 linux
               qwen2.5:32b-instruct-ggml-darwin-3a9b        default                      darwin
               qwen2.5:72b-instruct-ecd6                    default  80Gx2               linux
               qwen2.5:72b-instruct-awq-ff38                default  80G                 linux
               qwen2.5:72b-instruct-gptq-w8a8-d602          default  80G                 linux
               qwen2.5:72b-instruct-gptq-w4a16-2d10         default  80G                 linux
               qwen2.5:72b-instruct-ggml-q4-darwin-416f     default                      darwin
qwen2.5-coder  qwen2.5-coder:3b-instruct-728b               default  24G                 linux
               qwen2.5-coder:7b-instruct-cc36               default  24G                 linux
               qwen2.5-coder:7b-instruct-awq-4024           default  24G                 linux
               qwen2.5-coder:7b-instruct-gptq-w8a8-5ea1     default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-linux-39f3    default                      linux
               qwen2.5-coder:7b-instruct-gptq-w4a16-b64f    default  24G                 linux
               qwen2.5-coder:7b-instruct-ggml-darwin-fb11   default                      darwin
               qwen2.5-coder:14b-instruct-ea2c              default  40G                 linux
               qwen2.5-coder:14b-instruct-awq-6643          default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w8a8-6440    default  40G                 linux
               qwen2.5-coder:14b-instruct-gptq-w4a16-0d16   default  40G                 linux
               qwen2.5-coder:32b-instruct-f738              default  80G                 linux
qwq            qwq:32b-774e                                 default  80G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository. See [DEVELOPMENT.md](./.github/DEVELOPMENT.md) for more information.