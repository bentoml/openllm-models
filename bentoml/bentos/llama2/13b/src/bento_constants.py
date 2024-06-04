
CONSTANT_YAML = '''
alias:
- 13b
chat_template: llama-2-chat
engine_config:
  max_model_len: 1024
  model: meta-llama/Llama-2-13b-chat-hf
project: vllm-chat
service_config:
  name: llama2
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-a100
  traffic:
    timeout: 300

'''
