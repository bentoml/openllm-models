
CONSTANT_YAML = '''
chat_template: mistral-instruct
engine_config:
  dtype: half
  enforce_eager: true
  max_model_len: 1024
  model: TheBloke/Mistral-7B-Instruct-v0.1-AWQ
  quantization: awq
extra_labels:
  openllm_alias: 7b-4bit,7b-instruct-4bit
  openllm_hf_model_id: TheBloke/Mistral-7B-Instruct-v0.1-AWQ
project: vllm-chat
service_config:
  name: mistral
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
