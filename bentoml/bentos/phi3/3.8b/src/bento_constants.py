
CONSTANT_YAML = '''
alias:
- latest
- 3.8b
- mini
chat_template: phi-3
engine_config:
  dtype: half
  max_model_len: 4096
  model: microsoft/Phi-3-mini-4k-instruct
project: vllm-chat
service_config:
  name: phi3
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
