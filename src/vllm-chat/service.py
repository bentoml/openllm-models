from __future__ import annotations

import base64, io, logging, os, traceback, typing, argparse
import bentoml, yaml, fastapi, PIL.Image, fastapi.staticfiles as staticfiles, fastapi.responses as responses

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

STATIC_DIR = os.path.join(os.path.dirname(__file__), "ui")

with open(os.path.join(os.path.dirname(__file__), "openllm_config.yaml")) as f:
    PARAMETERS = yaml.safe_load(f)
ENGINE_CONFIG = PARAMETERS.get("engine_config", {})
SERVICE_CONFIG = PARAMETERS.get("service_config", {})
SERVER_CONFIG = PARAMETERS.get("server_config", {})
REQUIREMENTS_TXT = PARAMETERS.get("extra_requirements", [])

openai_api_app = fastapi.FastAPI()
ui_app = fastapi.FastAPI()
ui_app.mount("/static", staticfiles.StaticFiles(directory=STATIC_DIR), name="static")


@ui_app.get("/")
async def serve_chat_html():
    return responses.FileResponse(os.path.join(STATIC_DIR, "chat.html"))


@ui_app.get("/{full_path:path}")
async def catch_all(full_path: str):
    file_path = os.path.join(STATIC_DIR, full_path)
    if os.path.exists(file_path):
        return responses.FileResponse(file_path)
    return responses.FileResponse(os.path.join(STATIC_DIR, "chat.html"))


@bentoml.asgi_app(openai_api_app, path="/v1")
@bentoml.asgi_app(ui_app, path="/chat")
@bentoml.service(
    **SERVICE_CONFIG,
    image=bentoml.images.PythonImage(python_version="3.11")
    .python_packages("vllm==0.7.1", "pyyaml", "pillow", "openai", "bentoml>=1.3.20")
    .python_packages(*REQUIREMENTS_TXT),
)
class VLLM:
    model_id = ENGINE_CONFIG["model"]
    model = bentoml.models.HuggingFaceModel(model_id)

    def __init__(self) -> None:
        from vllm import AsyncEngineArgs, AsyncLLMEngine
        import vllm.entrypoints.openai.api_server as vllm_api_server
        from vllm.entrypoints.openai.serving_chat import OpenAIServingChat
        from vllm.entrypoints.openai.serving_models import BaseModelPath, OpenAIServingModels

        OPENAI_ENDPOINTS = [
            ["/chat/completions", vllm_api_server.create_chat_completion, ["POST"]],
            ["/models", vllm_api_server.show_available_models, ["GET"]],
        ]
        for route, endpoint, methods in OPENAI_ENDPOINTS:
            openai_api_app.add_api_route(
                path=route,
                endpoint=endpoint,
                methods=methods,
                include_in_schema=True,
            )

        ENGINE_ARGS = AsyncEngineArgs(**dict(ENGINE_CONFIG, model=self.model))
        self.engine = AsyncLLMEngine.from_engine_args(ENGINE_ARGS)
        logger.info(f"VLLM service initialized with model: {self.model_id}")

        model_config = self.engine.engine.get_model_config()

        args = argparse.Namespace()
        args.model = self.model
        args.disable_log_requests = True
        args.max_log_len = 1000
        args.response_role = "assistant"
        args.served_model_name = [self.model_id]
        args.chat_template = None
        args.chat_template_content_format = "auto"
        args.lora_modules = None
        args.prompt_adapters = None
        args.request_logger = None
        args.disable_log_stats = True
        args.return_tokens_as_token_ids = False
        args.enable_tool_call_parser = False
        args.enable_auto_tool_choice = False
        args.tool_call_parser = None
        args.enable_prompt_tokens_details = False
        args.enable_reasoning = False
        args.reasoning_parser = None

        for key, value in SERVICE_CONFIG.items():
            setattr(args, key, value)

        request_logger = None
        base_model_paths = [BaseModelPath(name=name, model_path=args.model) for name in args.served_model_name]

        openai_api_app.state.engine_client = self.engine
        openai_api_app.state.log_stats = False
        openai_api_app.state.openai_serving_models = OpenAIServingModels(
            engine_client=self.engine,
            model_config=model_config,
            base_model_paths=base_model_paths,
            lora_modules=args.lora_modules,
            prompt_adapters=args.prompt_adapters,
        )
        openai_api_app.state.openai_serving_chat = OpenAIServingChat(
            self.engine,
            model_config,
            openai_api_app.state.openai_serving_models,
            args.response_role,
            request_logger=request_logger,
            chat_template=args.chat_template,
            chat_template_content_format=args.chat_template_content_format,
            return_tokens_as_token_ids=args.return_tokens_as_token_ids,
            enable_auto_tools=args.enable_auto_tool_choice,
            tool_parser=args.tool_call_parser,
            enable_reasoning=args.enable_reasoning,
            reasoning_parser=args.reasoning_parser,
            enable_prompt_tokens_details=args.enable_prompt_tokens_details,
        )
        openai_api_app.state.task = model_config.task

    @bentoml.api
    async def generate(self, prompt: str = "what is this?") -> typing.AsyncGenerator[str, None]:
        from openai import AsyncOpenAI

        client = AsyncOpenAI(base_url="http://127.0.0.1:3000/v1", api_key="dummy")

        try:
            completion = await client.chat.completions.create(
                model=self.model_id,
                messages=[dict(role="user", content=[dict(type="text", text=prompt)])],
                stream=True,
            )
            async for chunk in completion:
                yield chunk.choices[0].delta.content or ""
        except Exception:
            yield traceback.format_exc()

    @bentoml.api
    async def sights(
        self, prompt: str = "what is this?", image: typing.Optional[PIL.Image.Image] = None
    ) -> typing.AsyncGenerator[str, None]:
        from openai import AsyncOpenAI

        client = AsyncOpenAI(base_url="http://127.0.0.1:3000/v1", api_key="dummy")
        if image:
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            buffered.close()
            image_url = f"data:image/png;base64,{img_str}"
            content = [
                dict(type="image_url", image_url=dict(url=image_url)),
                dict(type="text", text=prompt),
            ]
        else:
            content = [dict(type="text", text=prompt)]

        try:
            completion = await client.chat.completions.create(
                model=self.model_id,
                messages=[dict(role="user", content=content)],
                stream=True,
            )
            async for chunk in completion:
                yield chunk.choices[0].delta.content or ""
        except Exception:
            yield traceback.format_exc()
