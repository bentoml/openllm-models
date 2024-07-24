
CONSTANT_YAML = '''
chat_template: mistral-instruct
engine_config:
  max_model_len: 2048
  model: mistralai/Mixtral-8x7B-Instruct-v0.1
  tensor_parallel_size: 2
extra_labels:
  model_name: mistralai/Mixtral-8x7B-Instruct-v0.1
  openllm_alias: 8x7b,8x7b-instruct
project: vllm-chat
service_config:
  name: mixtral
  resources:
    gpu: 2
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
