
CONSTANT_YAML = '''
chat_template: llama-2-chat
engine_config:
  enforce_eager: true
  max_model_len: 1024
  model: TheBloke/Llama-2-7B-Chat-AWQ
  quantization: awq
extra_labels:
  model_name: TheBloke/Llama-2-7B-Chat-AWQ
  openllm_alias: 7b-4bit,7b-chat-4bit
project: vllm-chat
service_config:
  name: llama2
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
