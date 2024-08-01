
CONSTANT_YAML = '''
chat_template: mistral-instruct
engine_config:
  dtype: half
  max_model_len: 2048
  model: mistralai/Mistral-Large-Instruct-2407
  tensor_parallel_size: 4
extra_labels:
  model_name: mistralai/Mistral-Large-Instruct-2407
  openllm_alias: large,large-instruct, 123b, 123b-instruct
project: vllm-chat
service_config:
  name: mistral
  resources:
    gpu: 4
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
