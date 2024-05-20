
CONSTANT_YAML = '''
alias:
- 7b
- 7b-instruct
- 7b-instruct-v0.1
engine_config:
  enforce_eager: true
  max_model_len: 1024
  model: mistralai/Mistral-7B-Instruct-v0.1
project: vllm-chat
prompt:
  body: '<s>[INST]

    You are a helpful, respectful and honest assistant. Always answer as helpfully
    as possible, while being safe. Your answers should not include any harmful, unethical,
    racist, sexist, toxic, dangerous, or illegal content. Please ensure that your
    responses are socially unbiased and positive in nature.

    If a question does not make any sense, or is not factually coherent, explain why
    instead of answering something not correct. If you don''t know the answer to a
    question, please don''t share false information.

    {user_prompt} [/INST] '
  head: null
service_config:
  name: mistral
  resources:
    gpu: 1
    gpu_type: nvidia-tesla-l4
  traffic:
    timeout: 300

'''
