
CONSTANT_YAML = '''
alias:
- 2b
engine_config:
  max_model_len: 2048
  model: google/gemma-2b-it
project: vllm-chat
service_config:
  name: gemma
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
