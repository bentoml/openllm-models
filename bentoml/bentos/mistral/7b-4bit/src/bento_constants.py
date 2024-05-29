
CONSTANT_YAML = '''
alias:
- 7b-4bit
chat_template: mistral-instruct
engine_config:
  dtype: half
  enforce_eager: true
  max_model_len: 1024
  model: TheBloke/Mistral-7B-Instruct-v0.1-AWQ
  quantization: awq
project: vllm-chat
service_config:
  name: mistral
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
