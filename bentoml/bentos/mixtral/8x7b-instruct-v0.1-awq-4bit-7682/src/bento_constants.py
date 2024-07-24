
CONSTANT_YAML = '''
chat_template: mistral-instruct
engine_config:
  gpu_memory_utilization: 0.8
  max_model_len: 2048
  model: casperhansen/mixtral-instruct-awq
  quantization: awq
extra_labels:
  model_name: casperhansen/mixtral-instruct-awq
  openllm_alias: 8x7b-4bit
project: vllm-chat
service_config:
  name: mixtral
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-a100
  traffic:
    timeout: 300

'''
