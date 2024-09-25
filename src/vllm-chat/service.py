import functools
from openai import AsyncOpenAI
import PIL.Image
import json
import logging
import os
from typing import AsyncGenerator, Literal

import bentoml
import fastapi
import fastapi.staticfiles
import pydantic
import vllm.entrypoints.openai.api_server as vllm_api_server
import yaml
from annotated_types import Ge, Le
from fastapi.responses import FileResponse
from typing_extensions import Annotated, Literal


# Load the constants from the yaml file
CONSTANT_YAML = os.path.join(os.path.dirname(__file__), "openllm_config.yaml")
with open(CONSTANT_YAML) as f:
    PARAMETERS = yaml.safe_load(f)

ENGINE_CONFIG = PARAMETERS.get("vllm", {}).get("engine_args", {})
SERVICE_CONFIG = PARAMETERS.get("bentoml", {}).get("service_args", {})
OVERRIDE_CHAT_TEMPLATE = PARAMETERS.get("chat_template")

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

        if OVERRIDE_CHAT_TEMPLATE:  # use community chat template
            gen_config = _get_gen_config(OVERRIDE_CHAT_TEMPLATE)
            chat_template = gen_config["template"]
        else:
            chat_template = None

        model_config = self.engine.engine.get_model_config()

        # inject the engine into the openai serving chat and completion
        vllm_api_server.openai_serving_chat = OpenAIServingChat(
            async_engine_client=self.engine,
            served_model_names=[ENGINE_CONFIG["model"]],
            response_role="assistant",
            chat_template=chat_template,
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

    @bentoml.api(route="/api/chat")
    async def chat(
        self,
        image: PIL.Image.Image,
        prompt: str = "Describe the image",
        max_tokens: Annotated[
            int,
            Ge(128),
            Le(ENGINE_CONFIG["max_model_len"]),
        ] = ENGINE_CONFIG["max_model_len"],
    ) -> AsyncGenerator[str, None]:
        """
        light-weight chat API that takes in a list of messages and returns a response
        """
        import io
        import base64
    
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        img_b64_str = base64.b64encode(img_byte_arr).decode('utf-8')
        img_type = 'image/png'
    
        client = AsyncOpenAI(base_url="http://localhost:3000/v1")
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:{img_type};base64,{img_b64_str}"}},
                    ]
                },
            ],
            max_tokens=max_tokens,
            model=ENGINE_CONFIG["model"],
        )
        async for message in chat_completion.messages:
            yield message.content


@functools.lru_cache(maxsize=1)
def _get_gen_config(community_chat_template: str) -> dict:
    logger.info(f"Load community_chat_template: {community_chat_template}")
    chat_template_path = os.path.join(
        os.path.dirname(__file__), "chat_templates", "chat_templates"
    )
    config_path = os.path.join(
        os.path.dirname(__file__), "chat_templates", "generation_configs"
    )
    with open(os.path.join(config_path, f"{community_chat_template}.json")) as f:
        gen_config = json.load(f)
    chat_template_file = gen_config["chat_template"].split("/")[-1]
    with open(os.path.join(chat_template_path, chat_template_file)) as f:
        chat_template = f.read()
    gen_config["template"] = chat_template.replace("    ", "").replace("\n", "")
    return gen_config
