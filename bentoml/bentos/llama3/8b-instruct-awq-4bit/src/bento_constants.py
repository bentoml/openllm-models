
CONSTANT_YAML = '''
alias:
- 8b-4bit
engine_config:
  max_model_len: 2048
  model: casperhansen/llama-3-8b-instruct-awq
  quantization: awq
project: vllm-chat
service_config:
  name: llama3
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
