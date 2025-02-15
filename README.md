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
model                version                                         repo     required GPU RAM    platforms
-------------------  ----------------------------------------------  -------  ------------------  -----------
deepseek-r1          deepseek-r1:671b-b108                           default  80Gx16              linux
deepseek-r1-distill  deepseek-r1-distill:qwen2.5-14b-0f87            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-32b-0778            default  80G                 linux
                     deepseek-r1-distill:qwen2.5-7b-math-a793        default  24G                 linux
                     deepseek-r1-distill:llama3.1-8b-8ff8            default  24G                 linux
                     deepseek-r1-distill:llama3.3-70b-instruct-6c69  default  80Gx2               linux
deepseek-v3          deepseek-v3:671b-instruct-1f42                  default  80Gx16              linux
gemma2               gemma2:2b-instruct-cfb0                         default  12G                 linux
                     gemma2:9b-instruct-0fde                         default  24G                 linux
                     gemma2:27b-instruct-fbd5                        default  80G                 linux
jamba1.5             jamba1.5:mini-d429                              default  80Gx4               linux
llama3.1             llama3.1:8b-instruct-36aa                       default  24G                 linux
llama3.2             llama3.2:1b-instruct-69e9                       default  24G                 linux
                     llama3.2:3b-instruct-6020                       default  24G                 linux
                     llama3.2:11b-vision-instruct-dc13               default  80G                 linux
                     llama3.2:90b-vision-instruct-294c               default  80Gx2               linux
llama3.3             llama3.3:70b-instruct-ee45                      default  80Gx2               linux
mistral              mistral:8b-instruct-e4ac                        default  24G                 linux
mistral-large        mistral-large:123b-instruct-98c0                default  80Gx4               linux
                     mistral-large:123b-instruct-awq-4bit-c69a       default  80G                 linux
mistralai            mistralai:24b-small-instruct-2501-ed08          default  80G                 linux
mixtral              mixtral:8x7b-instruct-v0.1-f096                 default  80Gx2               linux
phi4                 phi4:14b-520a                                   default  80G                 linux
pixtral              pixtral:12b-240910-e9f7                         default  80G                 linux
qwen2.5              qwen2.5:7b-instruct-0165                        default  24G                 linux
                     qwen2.5:14b-instruct-4d71                       default  80G                 linux
                     qwen2.5:14b-instruct-ggml-q4-darwin-d883        default                      macos
                     qwen2.5:14b-instruct-ggml-q8-darwin-eb72        default                      macos
                     qwen2.5:32b-instruct-a679                       default  80G                 linux
                     qwen2.5:32b-instruct-awq-4bit-5776              default  40G                 linux
                     qwen2.5:32b-instruct-ggml-darwin-762d           default                      macos
                     qwen2.5:72b-instruct-4a76                       default  80Gx2               linux
                     qwen2.5:72b-instruct-ggml-q4-darwin-7132        default                      macos
qwen2.5-coder        qwen2.5-coder:7b-instruct-1753                  default  24G                 linux
                     qwen2.5-coder:7b-instruct-ggml-linux-1166       default                      linux
                     qwen2.5-coder:7b-instruct-ggml-darwin-1107      default                      macos
                     qwen2.5-coder:32b-instruct-44eb                 default  80G                 linux
qwen2.5vl            qwen2.5vl:3b-instruct-3838                      default  24G                 linux
                     qwen2.5vl:7b-instruct-0c0a                      default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.