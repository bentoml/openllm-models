
CONSTANT_YAML = '''
alias:
- 72b
engine_config:
  max_model_len: 2048
  model: Qwen/Qwen2-72B-Instruct
project: vllm-chat
service_config:
  name: qwen2
  resources:
    gpu: 2
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
