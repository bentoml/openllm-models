
CONSTANT_YAML = '''
alias:
- latest
- 8b
- 8b-instruct
engine_config:
  max_model_len: 2048
  model: meta-llama/Meta-Llama-3-8B-Instruct
project: vllm-chat
service_config:
  name: llama3
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-l4
  traffic:
    timeout: 300

'''
