
CONSTANT_YAML = '''
alias:
- 7b
engine_config:
  max_model_len: 2048
  model: google/gemma-7b-it
project: vllm-chat
service_config:
  name: gemma
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-l4
  traffic:
    timeout: 300

'''
