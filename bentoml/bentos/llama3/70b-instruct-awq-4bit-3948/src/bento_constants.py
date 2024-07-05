
CONSTANT_YAML = '''
engine_config:
  max_model_len: 2048
  model: casperhansen/llama-3-70b-instruct-awq
  quantization: awq
extra_labels:
  openllm_alias: 70b-4bit,70b-instruct-4bit
  openllm_hf_model_id: casperhansen/llama-3-70b-instruct-awq
project: vllm-chat
service_config:
  name: llama3
  resources:
    gpu: 1
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
