
CONSTANT_YAML = '''
chat_template: mistral-instruct
engine_config:
  dtype: half
  max_model_len: 2048
  model: casperhansen/mistral-large-instruct-2407-awq
extra_labels:
  model_name: casperhansen/mistral-large-instruct-2407-awq
  openllm_alias: large-4bit,large-instruct-4bit, 123b-4bit, 123b-instruct-4bit
project: vllm-chat
service_config:
  name: mistral
  resources:
    gpu: 1
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
