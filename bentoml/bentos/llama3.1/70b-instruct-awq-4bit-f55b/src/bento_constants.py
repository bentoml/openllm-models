
CONSTANT_YAML = '''
engine_config:
  max_model_len: 2048
  model: hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4
  quantization: awq
extra_labels:
  model_name: hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4
  openllm_alias: 70b-4bit,70b-instruct-4bit
project: vllm-chat
service_config:
  name: llama3.1
  resources:
    gpu: 1
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
