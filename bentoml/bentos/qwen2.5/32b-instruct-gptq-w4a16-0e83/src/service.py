from __future__ import annotations

import os, bentoml, typing, contextlib, logging, pydantic, fastapi, typing_extensions, annotated_types, fastapi.staticfiles as staticfiles, fastapi.responses as responses

logger = logging.getLogger("bentoml.service")


class BentoArgs(pydantic.BaseModel):
    openllm_model_id: str = "Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4"
    openllm_max_tokens: int = pydantic.Field(default_factory=lambda: int(os.environ.get("MAX_TOKENS", 2048)))

    disable_log_requests: bool = True
    max_log_len: int = 1000
    request_logger: typing.Any = None
    disable_log_stats: bool = True
    use_tqdm_on_load: bool = False
    task: str = pydantic.Field(default_factory=lambda: os.environ.get("TASK", "generate"))
    max_model_len: int = 20480
    tool_call_parser: str = "hermes"
    enable_auto_tool_choice: bool = True

    @pydantic.model_serializer
    def serialize_model(self) -> dict[str, typing.Any]:
        return {k: getattr(self, k) for k in self.__class__.model_fields if not k.startswith("openllm_")}


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
    name="qwen2.5",
    resources={"gpu": 1, "gpu_type": "nvidia-tesla-a100"},
    traffic={"timeout": 300},
    envs=[
        {"name": "UV_NO_PROGRESS", "value": "1"},
        {"name": "HF_HUB_DISABLE_PROGRESS_BARS", "value": "1"},
        {"name": "VLLM_ATTENTION_BACKEND", "value": "FLASH_ATTN"},
        {"name": "VLLM_USE_V1", "value": "1"},
    ],
    labels=dict(generator="openllm", owner="bentoml-team", aliases="32b-w4a16"),
    image=bentoml.images.Image(python_version="3.11", lock_python_packages=False)
    .requirements_file("requirements.txt")
    .run("uv pip install --compile-bytecode flashinfer-python --find-links https://flashinfer.ai/whl/cu124/torch2.6"),
)
class LLM:
    model = bentoml.models.HuggingFaceModel(bento_args.openllm_model_id, exclude=["*.pth", "*.pt", "original/**/*"])

    def __init__(self):
        from openai import AsyncOpenAI

        self.openai = AsyncOpenAI(base_url="http://127.0.0.1:3000/v1", api_key="dummy")
        self.exit_stack = contextlib.AsyncExitStack()

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

        engine = await self.exit_stack.enter_async_context(vllm_api_server.build_async_engine_client(args))
        model_config = await engine.get_model_config()

        await vllm_api_server.init_app_state(engine, model_config, openai_api_app.state, args)

    @bentoml.on_shutdown
    async def teardown_engine(self):
        await self.exit_stack.aclose()

    @bentoml.api
    async def generate(
        self,
        prompt: str = "Who are you? Please respond in pirate speak!",
        max_tokens: typing_extensions.Annotated[
            int, annotated_types.Ge(128), annotated_types.Le(bento_args.openllm_max_tokens)
        ] = bento_args.openllm_max_tokens,
    ) -> typing.AsyncGenerator[str, None]:
        messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
        try:
            completion = await self.openai.chat.completions.create(
                model=bento_args.openllm_model_id, messages=messages, stream=True, max_tokens=max_tokens
            )
            async for chunk in completion:
                yield chunk.choices[0].delta.content or ""
        except Exception:
            logger.error(traceback.format_exc())
            yield "Internal error found. Check server logs for more information"
            return
