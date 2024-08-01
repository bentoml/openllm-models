
CONSTANT_YAML = '''
engine_config:
  dtype: half
  max_model_len: 2048
  model: google/gemma-2-27b-it
extra_envs:
- name: VLLM_ATTENTION_BACKEND
  value: FLASHINFER
extra_labels:
  model_name: google/gemma-2-27b-it
  openllm_alias: 27b,27b-instruct
extra_requirements:
- --extra-index-url https://flashinfer.ai/whl/cu121/torch2.3
- flashinfer
project: vllm-chat
service_config:
  name: gemma2
  resources:
    gpu: 1
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
