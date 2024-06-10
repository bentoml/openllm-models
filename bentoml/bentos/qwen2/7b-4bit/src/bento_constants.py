
CONSTANT_YAML = '''
alias:
- 7b-4bit
engine_config:
  max_model_len: 2048
  model: Qwen/Qwen2-7B-Instruct-AWQ
  quantization: awq
project: vllm-chat
service_config:
  name: qwen2
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
