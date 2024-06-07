
CONSTANT_YAML = '''
alias:
- 70b-4bit
engine_config:
  max_model_len: 2048
  model: Qwen/Qwen2-72B-Instruct-AWQ
  quantization: awq
project: vllm-chat
service_config:
  name: qwen2
  resources:
    gpu: 1
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
