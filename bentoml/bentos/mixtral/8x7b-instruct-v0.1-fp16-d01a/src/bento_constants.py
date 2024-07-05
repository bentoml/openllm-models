
CONSTANT_YAML = '''
chat_template: mistral-instruct
engine_config:
  max_model_len: 2048
  model: mistralai/Mixtral-8x7B-Instruct-v0.1
extra_labels:
  openllm_alias: 8x7b,8x7b-instruct
  openllm_hf_model_id: mistralai/Mixtral-8x7B-Instruct-v0.1
project: vllm-chat
service_config:
  name: mixtral
  resources:
    gpu: 2
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
