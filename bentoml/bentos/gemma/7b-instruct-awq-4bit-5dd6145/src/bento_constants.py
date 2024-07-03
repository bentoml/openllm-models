
CONSTANT_YAML = '''
chat_template: gemma-it
engine_config:
  max_model_len: 2048
  model: casperhansen/gemma-7b-it-awq
  quantization: awq
extra_labels:
  openllm_alias: 7b-4bit,7b-instruct-4bit
  openllm_hf_model_id: casperhansen/gemma-7b-it-awq
project: vllm-chat
service_config:
  name: gemma
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
