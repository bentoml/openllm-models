
CONSTANT_YAML = '''
engine_config:
  dtype: half
  max_model_len: 2048
  model: meta-llama/Meta-Llama-3.1-8B-Instruct
extra_labels:
  model_name: meta-llama/Meta-Llama-3.1-8B-Instruct
  openllm_alias: 8b,8b-instruct
project: vllm-chat
service_config:
  name: llama3.1
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-l4
  traffic:
    timeout: 300

'''
