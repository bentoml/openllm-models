
CONSTANT_YAML = '''
engine_config:
  max_model_len: 2048
  model: meta-llama/Meta-Llama-3-70B-Instruct
extra_labels:
  openllm_alias: 70b,70b-instruct
  openllm_hf_model_id: meta-llama/Meta-Llama-3-70B-Instruct
project: vllm-chat
service_config:
  name: llama3
  resources:
    gpu: 2
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
