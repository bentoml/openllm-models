
CONSTANT_YAML = '''
engine_config:
  dtype: half
  max_model_len: 2048
  model: google/gemma-2b-it
extra_labels:
  openllm_alias: 2b,2b-instruct
  openllm_hf_model_id: google/gemma-2b-it
project: vllm-chat
service_config:
  name: gemma
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
