
CONSTANT_YAML = '''
alias: []
engine_config:
  enforce_eager: true
  max_model_len: 1024
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
