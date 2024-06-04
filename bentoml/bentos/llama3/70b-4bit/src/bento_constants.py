
CONSTANT_YAML = '''
alias:
- 70b-4bit
engine_config:
  max_model_len: 2048
  model: casperhansen/llama-3-70b-instruct-awq
  quantization: awq
project: vllm-chat
service_config:
  name: llama3
  resources:
    gpu: 1
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
