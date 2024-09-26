import logging
import os
from argparse import Namespace
from typing import Literal

import bentoml
import fastapi
import fastapi.staticfiles
import pydantic
import vllm.entrypoints.openai.api_server as vllm_api_server
import yaml
from fastapi.responses import FileResponse


class Message(pydantic.BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Load the constants from the yaml file
PARAMETER_YAML = os.path.join(os.path.dirname(__file__), "openllm_config.yaml")
with open(PARAMETER_YAML) as f:
    PARAMETERS = yaml.safe_load(f)

ENGINE_CONFIG = PARAMETERS.get("vllm", {}).get("engine_args", {})
SERVICE_CONFIG = PARAMETERS.get("bentoml", {}).get("service_args", {})


# openai api app
openai_api_app = fastapi.FastAPI()
OPENAI_ENDPOINTS = [
    ["/chat/completions", vllm_api_server.create_chat_completion, ["POST"]],
    ["/completions", vllm_api_server.create_completion, ["POST"]],
    ["/models", vllm_api_server.show_available_models, ["GET"]],
]
for route, endpoint, methods in OPENAI_ENDPOINTS:
    openai_api_app.add_api_route(
        path=route,
        endpoint=endpoint,
        methods=methods,
        include_in_schema=True,
    )


# chat UI app
ui_app = fastapi.FastAPI()
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
        from vllm.entrypoints.openai.api_server import init_app_state

        ENGINE_ARGS = AsyncEngineArgs(**ENGINE_CONFIG)
        self.engine = AsyncLLMEngine.from_engine_args(ENGINE_ARGS)
        logger.info(f"VLLM service initialized with model: {ENGINE_CONFIG['model']}")

        model_config = self.engine.engine.get_model_config()

        args = Namespace()
        args.model = ENGINE_CONFIG["model"]
        args.disable_log_requests = True
        args.max_log_len = 1000
        args.response_role = "assistant"
        args.served_model_name = None
        args.chat_template = None
        args.lora_modules = None
        args.prompt_adapters = None
        args.request_logger = None
        args.disable_log_stats = True
        args.return_tokens_as_token_ids = False
        args.enable_tool_call_parser = False
        args.enable_auto_tool_choice = False
        args.tool_call_parser = None

        init_app_state(self.engine, model_config, openai_api_app.state, args)
