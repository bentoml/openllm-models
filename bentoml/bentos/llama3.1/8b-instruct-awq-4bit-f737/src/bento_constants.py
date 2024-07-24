
CONSTANT_YAML = '''
engine_config:
  max_model_len: 2048
  model: hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4
  quantization: awq
extra_labels:
  model_name: hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4
  openllm_alias: 8b-4bit,8b-instruct-4bit
project: vllm-chat
service_config:
  name: llama3.1
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
