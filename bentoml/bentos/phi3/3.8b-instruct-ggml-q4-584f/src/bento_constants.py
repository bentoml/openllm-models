
CONSTANT_YAML = '''
chat_template: phi-3
engine_config:
  max_model_len: 2048
  model: microsoft/Phi-3-mini-4k-instruct-gguf
extra_labels:
  openllm_alias: 3.8b-q4,3.8b-mini-q4,3.8b-mini-instruct-4k-ggml-q4
  openllm_hf_model_id: microsoft/Phi-3-mini-4k-instruct-gguf
project: llamacpp-chat
service_config:
  name: phi3
  resources:
    memory: 3Gi
  traffic:
    timeout: 300

'''
