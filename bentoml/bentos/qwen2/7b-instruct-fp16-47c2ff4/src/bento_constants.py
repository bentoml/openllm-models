
CONSTANT_YAML = '''
engine_config:
  dtype: half
  max_model_len: 2048
  model: Qwen/Qwen2-7B-Instruct
extra_labels:
  openllm_alias: 7b,7b-instruct
  openllm_hf_model_id: Qwen/Qwen2-7B-Instruct
project: vllm-chat
service_config:
  name: qwen2
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-l4
  traffic:
    timeout: 300

'''
