
CONSTANT_YAML = '''
engine_config:
  max_model_len: 2048
  model: casperhansen/llama-3-8b-instruct-awq
  quantization: awq
extra_labels:
  model_name: casperhansen/llama-3-8b-instruct-awq
  openllm_alias: 8b-4bit,8b-instruct-4bit
project: vllm-chat
service_config:
  name: llama3
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
