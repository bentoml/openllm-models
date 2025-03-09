from __future__ import annotations

import os, json, typing, typing_extensions, annotated_types
import yaml, bentoml, pydantic, fastapi, fastapi.staticfiles, fastapi.responses

SYS_PROMPT = """
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content.
Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.If you don't know the answer to a question, please don't share false information
"""

# Load the constants from the yaml file
CONSTANT_YAML = os.path.join(os.path.dirname(__file__), "openllm-config.yaml")
with open(CONSTANT_YAML) as f:
    CONSTANTS = yaml.safe_load(f)

ENGINE_CONFIG = CONSTANTS["engine_config"]
SERVICE_CONFIG = CONSTANTS["service_config"]


class Message(pydantic.BaseModel):
    role: typing.Literal["system", "user", "assistant"]
    content: str


STATIC_DIR = os.path.join(os.path.dirname(__file__), "ui")

static_app = fastapi.FastAPI()
ui_app = fastapi.FastAPI()
openai_api_app = fastapi.FastAPI()


@openai_api_app.get("/models")
async def show_available_models():
    # Return the available models
    return {
        "data": [{"id": ENGINE_CONFIG["repo_id"], "object": "model", "created": 1686935002, "owned_by": "bentoml"}]
    }


ui_app.mount("/static", fastapi.staticfiles.StaticFiles(directory=STATIC_DIR), name="static")


@ui_app.get("/")
async def serve_chat_html():
    return fastapi.responses.FileResponse(os.path.join(STATIC_DIR, "chat.html"))


@ui_app.get("/{full_path:path}")
async def catch_all(full_path: str):
    file_path = os.path.join(STATIC_DIR, full_path)
    if os.path.exists(file_path):
        return fastapi.responses.FileResponse(file_path)
    return fastapi.responses.FileResponse(os.path.join(STATIC_DIR, "chat.html"))


@bentoml.mount_asgi_app(ui_app, path="/chat")
@bentoml.mount_asgi_app(openai_api_app, path="/v1")
@bentoml.service(**SERVICE_CONFIG)
class LlamaCppChat:
    model = bentoml.models.HuggingFaceModel(ENGINE_CONFIG["repo_id"])

    def __init__(self) -> None:
        from llama_cpp import Llama

        self.llm = Llama.from_pretrained(**ENGINE_CONFIG)

    @bentoml.api(route="/v1/chat/completions")
    async def chat_completions(
        self,
        messages: typing.List[Message] = [{"role": "user", "content": "What is the meaning of life?"}],
        model: str = ENGINE_CONFIG["repo_id"],
        max_tokens: typing_extensions.Annotated[
            int, annotated_types.Ge(128), annotated_types.Le(ENGINE_CONFIG["max_model_len"])
        ] = ENGINE_CONFIG["max_model_len"],
        stop: typing.Optional[typing.List[str]] = None,
        stream: typing.Optional[bool] = True,
        temperature: typing.Optional[float] = 0,
        top_p: typing.Optional[float] = 1.0,
        frequency_penalty: typing.Optional[float] = 0.0,
    ) -> typing.AsyncGenerator[str, None]:
        """
        Chat API that takes in a list of messages and returns a response
        """
        try:
            response = self.llm.create_chat_completion(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                stream=stream,
                stop=stop,
                temperature=temperature,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
            )
            if not stream:
                yield json.dumps(response)
                return

            for chunk in response:
                try:
                    json_srt = json.dumps(chunk)
                    yield f"data: {json_srt}"
                except Exception as e:
                    print(e)
                    yield "data: Internal error. Check server logs"
                    yield "data: [DONE]"
                    return

            yield "data: [DONE]"
        except Exception as e:
            print(e)
            yield "data: Internal error. Check server logs"
            yield "data: [DONE]"
