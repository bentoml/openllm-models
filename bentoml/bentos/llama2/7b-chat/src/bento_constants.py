
CONSTANT_YAML = '''
alias:
- latest
- 7b
- 7b-chat
engine_config:
  max_model_len: 1024
  model: meta-llama/Llama-2-7b-chat-hf
project: vllm-chat
prompt:
  body: '<s>[INST] <<SYS>>

    You are a helpful, respectful and honest assistant. Always answer as helpfully
    as possible, while being safe. Your answers should not include any harmful, unethical,
    racist, sexist, toxic, dangerous, or illegal content. Please ensure that your
    responses are socially unbiased and positive in nature.

    If a question does not make any sense, or is not factually coherent, explain why
    instead of answering something not correct. If you don''t know the answer to a
    question, please don''t share false information.

    <</SYS>>

    {user_prompt} [/INST] '
  head: null
service_config:
  name: llama2
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-t4
  traffic:
    timeout: 300

'''
