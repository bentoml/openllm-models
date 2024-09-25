import logging
import os
from typing import Literal

import bentoml
import fastapi
import fastapi.staticfiles
import pydantic
import vllm.entrypoints.openai.api_server as vllm_api_server
import yaml
from fastapi.responses import FileResponse


# Load the constants from the yaml file
CONSTANT_YAML = os.path.join(os.path.dirname(__file__), "openllm_config.yaml")
with open(CONSTANT_YAML) as f:
    PARAMETERS = yaml.safe_load(f)

ENGINE_CONFIG = PARAMETERS.get("vllm", {}).get("engine_args", {})
SERVICE_CONFIG = PARAMETERS.get("bentoml", {}).get("service_args", {})

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


openai_api_app = fastapi.FastAPI()
static_app = fastapi.FastAPI()
ui_app = fastapi.FastAPI()


OPENAI_ENDPOINTS = [
    ["/chat/completions", vllm_api_server.create_chat_completion, ["POST"]],
    ["/completions", vllm_api_server.create_completion, ["POST"]],
    ["/models", vllm_api_server.show_available_models, ["GET"]],
]


class Message(pydantic.BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


for route, endpoint, methods in OPENAI_ENDPOINTS:
    openai_api_app.add_api_route(
        path=route,
        endpoint=endpoint,
        methods=methods,
        include_in_schema=True,
    )


STATIC_DIR = os.path.join(os.path.dirname(__file__), "ui")

ui_app.mount(
    "/static", fastapi.staticfiles.StaticFiles(directory=STATIC_DIR), name="static"
)


@ui_app.get("/")
async def serve_chat_html():
    return FileResponse(os.path.join(STATIC_DIR, "chat.html"))


@ui_app.get("/{full_path:path}")
async def catch_all(full_path: str):
    file_path = os.path.join(STATIC_DIR, full_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return FileResponse(os.path.join(STATIC_DIR, "chat.html"))


@bentoml.mount_asgi_app(openai_api_app, path="/v1")
@bentoml.mount_asgi_app(ui_app, path="/chat")
@bentoml.service(**SERVICE_CONFIG)
class VLLM:
    def __init__(self) -> None:
        from vllm import AsyncEngineArgs, AsyncLLMEngine
        from vllm.entrypoints.openai.serving_chat import OpenAIServingChat
        from vllm.entrypoints.openai.serving_completion import OpenAIServingCompletion

        ENGINE_ARGS = AsyncEngineArgs(**ENGINE_CONFIG)
        self.engine = AsyncLLMEngine.from_engine_args(ENGINE_ARGS)
        logger.info(f"VLLM service initialized with model: {ENGINE_CONFIG['model']}")

        model_config = self.engine.engine.get_model_config()

        # inject the engine into the openai serving chat and completion
        vllm_api_server.openai_serving_chat = OpenAIServingChat(
            async_engine_client=self.engine,
            served_model_names=[ENGINE_CONFIG["model"]],
            response_role="assistant",
            chat_template=None,
            model_config=model_config,
            lora_modules=None,
            prompt_adapters=None,
            request_logger=None,
        )
        vllm_api_server.openai_serving_completion = OpenAIServingCompletion(
            async_engine_client=self.engine,
            served_model_names=[ENGINE_CONFIG["model"]],
            model_config=model_config,
            lora_modules=None,
            prompt_adapters=None,
            request_logger=None,
        )
