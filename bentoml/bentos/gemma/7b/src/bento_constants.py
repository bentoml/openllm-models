
CONSTANT_YAML = '''
alias:
- latest
- 7b
- 7b-instruct
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
