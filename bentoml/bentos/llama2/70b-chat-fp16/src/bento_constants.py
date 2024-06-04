
CONSTANT_YAML = '''
alias:
- 70b
chat_template: llama-2-chat
engine_config:
  max_model_len: 1024
  model: meta-llama/Llama-2-70b-chat-hf
project: vllm-chat
service_config:
  name: llama2
  resources:
    gpu: 2
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
