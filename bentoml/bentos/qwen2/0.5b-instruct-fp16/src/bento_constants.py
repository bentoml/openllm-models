
CONSTANT_YAML = '''
alias:
- 0.5b
engine_config:
  max_model_len: 2048
  model: Qwen/Qwen2-0.5B-Instruct
project: vllm-chat
service_config:
  name: qwen2
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
