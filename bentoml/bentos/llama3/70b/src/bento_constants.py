
CONSTANT_YAML = '''
alias:
- latest
- 70b
engine_config:
  max_model_len: 2048
  model: meta-llama/Meta-Llama-3-70B-Instruct
project: vllm-chat
service_config:
  name: llama3
  resources:
    gpu: 2
    gpu_type: nvidia-a100-80g
  traffic:
    timeout: 300

'''
