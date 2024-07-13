
CONSTANT_YAML = '''
chat_template: phi-3
engine_config:
  max_model_len: 2048
  model: microsoft/Phi-3-mini-4k-instruct-gguf
extra_labels:
  model_name: microsoft/Phi-3-mini-4k-instruct-gguf
  openllm_alias: 3.8b-ggml-q4,3.8b-mini-instruct-4k-ggml-q4
project: llamacpp-chat
service_config:
  name: phi3
  resources:
    memory: 3Gi
  traffic:
    timeout: 300

'''
