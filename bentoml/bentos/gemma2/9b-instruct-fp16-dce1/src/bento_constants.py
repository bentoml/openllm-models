
CONSTANT_YAML = '''
engine_config:
  dtype: half
  max_model_len: 2048
  model: google/gemma-2-9b-it
extra_envs:
- name: VLLM_ATTENTION_BACKEND
  value: FLASHINFER
extra_labels:
  model_name: google/gemma-2-9b-it
  openllm_alias: 9b,9b-instruct
extra_requirements:
- --extra-index-url https://flashinfer.ai/whl/cu121/torch2.3
- flashinfer
project: vllm-chat
service_config:
  name: gemma2
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-l4
  traffic:
    timeout: 300

'''
