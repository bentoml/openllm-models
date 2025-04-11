from __future__ import annotations

import os, bentoml, typing, pydantic, fastapi, fastapi.staticfiles as staticfiles, fastapi.responses as responses


class BentoArgs(pydantic.BaseModel):
    openllm_model_id: str = "Qwen/Qwen2.5-Coder-3B-Instruct"

    disable_log_requests: bool = True
    max_log_len: int = 1000
    request_logger: typing.Any = None
    disable_log_stats: bool = True
    use_tqdm_on_load: bool = False
    task: str = pydantic.Field(default_factory=lambda: os.environ.get("TASK", "generate"))
    max_model_len: int = 8192
    enable_auto_tool_choice: bool = True
    enable_tool_call_parser: bool = True
    tool_call_parser: str = "hermes"


bento_args = bentoml.use_arguments(BentoArgs)
openai_api_app = fastapi.FastAPI()
ui_app = fastapi.FastAPI()

STATIC_DIR = os.path.join(os.path.dirname(__file__), "ui")
ui_app.mount("/static", staticfiles.StaticFiles(directory=STATIC_DIR), name="static")


@ui_app.get("/")
async def serve_chat_html():
    return responses.FileResponse(os.path.join(STATIC_DIR, "chat.html"))


@ui_app.get("/{full_path:path}")
async def catch_all(full_path: str):
    if os.path.exists((file_path := os.path.join(STATIC_DIR, full_path))):
        return responses.FileResponse(file_path)
    return responses.FileResponse(os.path.join(STATIC_DIR, "chat.html"))


@bentoml.asgi_app(openai_api_app, path="/v1")
@bentoml.asgi_app(ui_app, path="/chat")
@bentoml.service(
    name="qwen2.5-coder",
    resources={"gpu": 1, "gpu_type": "nvidia-l4"},
    traffic={"timeout": 300},
    envs=[
        {"name": "UV_NO_PROGRESS", "value": "1"},
        {"name": "HF_HUB_DISABLE_PROGRESS_BARS", "value": "1"},
        {"name": "VLLM_ATTENTION_BACKEND", "value": "FLASH_ATTN"},
        {"name": "VLLM_USE_V1", "value": "1"},
    ],
    labels=dict(generator="openllm", owner="bentoml-team", aliases="3b"),
    image=bentoml.images.Image(python_version="3.11", lock_python_packages=False)
    .requirements_file("requirements.txt")
    .run("uv pip install --compile-bytecode flashinfer-python --find-links https://flashinfer.ai/whl/cu124/torch2.6"),
)
class LLM:
    model = bentoml.models.HuggingFaceModel(bento_args.openllm_model_id, exclude=["*.pth", "*.pt", "original/**/*"])

    @bentoml.on_startup
    async def init_engine(self) -> None:
        import vllm.entrypoints.openai.api_server as vllm_api_server

        from vllm.utils import FlexibleArgumentParser
        from vllm.entrypoints.openai.cli_args import make_arg_parser

        args = make_arg_parser(FlexibleArgumentParser()).parse_args([])
        args.model = self.model
        args.served_model_name = [bento_args.openllm_model_id]
        for key, value in bento_args.model_dump().items():
            setattr(args, key, value)

        router = fastapi.APIRouter(lifespan=vllm_api_server.lifespan)
        OPENAI_ENDPOINTS = [
            ["/models", vllm_api_server.show_available_models, ["GET"]],
            ["/chat/completions", vllm_api_server.create_chat_completion, ["POST"]],
            ["/embeddings", vllm_api_server.create_embedding, ["POST"]],
            ["/completions", vllm_api_server.create_completion, ["POST"]],
        ]

        for route, endpoint, methods in OPENAI_ENDPOINTS:
            router.add_api_route(path=route, endpoint=endpoint, methods=methods, include_in_schema=True)
        openai_api_app.include_router(router)

        self.engine_context = vllm_api_server.build_async_engine_client(args)
        self.engine = await self.engine_context.__aenter__()
        self.model_config = await self.engine.get_model_config()

        await vllm_api_server.init_app_state(self.engine, self.model_config, openai_api_app.state, args)

    @bentoml.on_shutdown
    async def teardown_engine(self):
        await self.engine_context.__aexit__(GeneratorExit, None, None)
