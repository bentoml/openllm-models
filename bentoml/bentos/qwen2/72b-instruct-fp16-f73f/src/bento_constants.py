
CONSTANT_YAML = '''
engine_config:
  dtype: half
  max_model_len: 2048
  model: Qwen/Qwen2-72B-Instruct
  tensor_parallel_size: 2
extra_labels:
  model_name: Qwen/Qwen2-72B-Instruct
  openllm_alias: 72b,72b-instruct
project: vllm-chat
service_config:
  name: qwen2
  resources:
    gpu: 2
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
