
CONSTANT_YAML = '''
engine_config:
  dtype: half
  max_model_len: 2048
  model: Qwen/Qwen2-57B-A14B-Instruct
extra_labels:
  openllm_alias: 57b-a14b,57b-a14b-instruct
  openllm_hf_model_id: Qwen/Qwen2-57B-A14B-Instruct
project: vllm-chat
service_config:
  name: qwen2
  resources:
    gpu: 2
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
