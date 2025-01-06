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
model              version                                          repo     required GPU RAM    platforms
-----------------  -----------------------------------------------  -------  ------------------  -----------
codestral          codestral:22b-v0.1-fp16-e452                     default  80G                 linux
gemma              gemma:2b-instruct-fp16-5eac                      default  12G                 linux
                   gemma:7b-instruct-fp16-c20f                      default  24G                 linux
                   gemma:7b-instruct-awq-4bit-80de                  default  12G                 linux
gemma2             gemma2:9b-instruct-fp16-aadd                     default  24G                 linux
                   gemma2:27b-instruct-fp16-376d                    default  80G                 linux
jamba1.5           jamba1.5:mini-fp16-dddc                          default  80Gx4               linux
llama2             llama2:7b-chat-fp16-3a8c                         default  16G                 linux
                   llama2:7b-chat-awq-4bit-0c30                     default  12G                 linux
                   llama2:13b-chat-fp16-e833                        default  40G                 linux
                   llama2:70b-chat-fp16-30af                        default  80Gx2               linux
llama3             llama3:8b-instruct-fp16-7dd1                     default  24G                 linux
                   llama3:8b-instruct-awq-4bit-0947                 default  12G                 linux
                   llama3:70b-instruct-fp16-2370                    default  80Gx2               linux
                   llama3:70b-instruct-awq-4bit-b148                default  80G                 linux
llama3.1           llama3.1:8b-instruct-fp16-210e                   default  24G                 linux
                   llama3.1:8b-instruct-awq-4bit-508e               default  12G                 linux
                   llama3.1:70b-instruct-fp16-5526                  default  80Gx2               linux
                   llama3.1:70b-instruct-awq-4bit-3330              default  80G                 linux
                   llama3.1:405b-instruct-awq-4bit-3f82             default  80Gx4               linux
llama3.1-nemotron  llama3.1-nemotron:70b-instruct-fp16-51b4         default  80Gx2               linux
llama3.2           llama3.2:1b-instruct-fp16-69ad                   default  12G                 linux
                   llama3.2:1b-instruct-ggml-fp16-linux-08c5        default                      linux
                   llama3.2:1b-instruct-ggml-fp16-darwin-12f1       default                      macos
                   llama3.2:3b-instruct-fp16-785f                   default  12G                 linux
                   llama3.2:11b-vision-instruct-1fbd                default  80G                 linux
llama3.3           llama3.3:70b-instruct-fp16-a20b                  default  80Gx2               linux
mistral            mistral:7b-instruct-fp16-28ad                    default  24G                 linux
                   mistral:7b-instruct-awq-4bit-f24d                default  12G                 linux
                   mistral:24b-instruct-nemo-e080                   default  80G                 linux
mistral-large      mistral-large:123b-instruct-fp16-c0fa            default  80Gx4               linux
                   mistral-large:123b-instruct-awq-4bit-a39f        default  80G                 linux
mixtral            mixtral:8x7b-instruct-v0.1-fp16-e7ea             default  80Gx2               linux
                   mixtral:8x7b-instruct-v0.1-awq-4bit-29b9         default  40G                 linux
phi3               phi3:3.8b-instruct-fp16-bdd2                     default  12G                 linux
                   phi3:3.8b-instruct-ggml-q4-ccda                  default                      macos
pixtral            pixtral:12b-240910-8551                          default  80G                 linux
qwen2              qwen2:0.5b-instruct-fp16-7c8c                    default  12G                 linux
                   qwen2:1.5b-instruct-fp16-32de                    default  12G                 linux
                   qwen2:7b-instruct-fp16-c1fc                      default  24G                 linux
                   qwen2:7b-instruct-awq-4bit-78b4                  default  12G                 linux
                   qwen2:57b-a14b-instruct-fp16-b977                default  80Gx2               linux
                   qwen2:72b-instruct-fp16-d6dc                     default  80Gx2               linux
                   qwen2:72b-instruct-awq-4bit-7a98                 default  80G                 linux
qwen2.5            qwen2.5:0.5b-instruct-fp16-3fbc                  default  12G                 linux
                   qwen2.5:1.5b-instruct-fp16-fba6                  default  12G                 linux
                   qwen2.5:3b-instruct-fp16-453b                    default  12G                 linux
                   qwen2.5:7b-instruct-fp16-b253                    default  24G                 linux
                   qwen2.5:14b-instruct-fp16-7f0b                   default  80G                 linux
                   qwen2.5:14b-instruct-ggml-q4-darwin-5f24         default                      macos
                   qwen2.5:14b-instruct-ggml-q8-darwin-8b4f         default                      macos
                   qwen2.5:32b-instruct-fp16-61fc                   default  80G                 linux
                   qwen2.5:32b-instruct-awq-4bit-f482               default  40G                 linux
                   qwen2.5:32b-instruct-ggml-fp16-darwin-028b       default                      macos
                   qwen2.5:72b-instruct-fp16-87a8                   default  80Gx2               linux
                   qwen2.5:72b-instruct-ggml-q4-darwin-7e2c         default                      macos
qwen2.5-coder      qwen2.5-coder:7b-instruct-9c7d                   default  24G                 linux
                   qwen2.5-coder:7b-instruct-ggml-fp16-linux-6e86   default                      linux
                   qwen2.5-coder:7b-instruct-ggml-fp16-darwin-dc3a  default                      macos
                   qwen2.5-coder:32b-instruct-109c                  default  80G                 linux
qwen2vl            qwen2vl:7b-instruct-fp16-ceb2                    default  24G                 linux

```

</td>
</tr>
</table>


## Development Guide

Open PRs to the `nightly` branch to add new models or update existing models.

You can also fork this repo and add your own models.

Use `openllm repo add` to use your own model repository.