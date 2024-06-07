
CONSTANT_YAML = '''
alias:
- 7b
engine_config:
  max_model_len: 2048
  model: Qwen/Qwen2-7B-Instruct
project: vllm-chat
service_config:
  name: qwen2
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-l4
  traffic:
    timeout: 300

'''
