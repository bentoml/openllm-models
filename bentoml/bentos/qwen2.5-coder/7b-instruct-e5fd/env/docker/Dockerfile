# ===========================================
#
# THIS IS A GENERATED DOCKERFILE. DO NOT EDIT
#
# ===========================================

# Block SETUP_BENTO_BASE_IMAGE
FROM python:3.11-slim AS base-container

ENV LANG=C.UTF-8

ENV LC_ALL=C.UTF-8

ENV PYTHONIOENCODING=UTF-8

ENV PYTHONUNBUFFERED=1

ARG BENTO_USER=bentoml
ARG BENTO_USER_UID=1034
ARG BENTO_USER_GID=1034
RUN groupadd -g $BENTO_USER_GID -o $BENTO_USER && useradd -m -u $BENTO_USER_UID -g $BENTO_USER_GID -o -r $BENTO_USER


ARG BENTO_PATH=/home/bentoml/bento
ENV BENTO_PATH=$BENTO_PATH
ENV BENTOML_HOME=/home/bentoml/
ENV BENTOML_HF_CACHE_DIR=/home/bentoml/bento/hf-models
ENV BENTOML_CONTAINERIZED=true

ARG UV_NO_PROGRESS=1
ENV UV_NO_PROGRESS=$UV_NO_PROGRESS
ARG HF_HUB_DISABLE_PROGRESS_BARS=1
ENV HF_HUB_DISABLE_PROGRESS_BARS=$HF_HUB_DISABLE_PROGRESS_BARS
ARG VLLM_LOGGING_CONFIG_PATH=/tmp/tmpon5_q2qd/logging-config.json
ENV VLLM_LOGGING_CONFIG_PATH=$VLLM_LOGGING_CONFIG_PATH

RUN mkdir $BENTO_PATH && chown bentoml:bentoml $BENTO_PATH -R
WORKDIR $BENTO_PATH

COPY --chown=bentoml:bentoml ./env/docker ./env/docker/
RUN export UV_COMPILE_BYTECODE=1
RUN apt-get update && apt-get install -q -y --no-install-recommends --allow-remove-essential ca-certificates gnupg2 bash build-essential git
RUN command -v uv >/dev/null || pip install uv
RUN UV_PYTHON_INSTALL_DIR=/app/python/ uv venv --python 3.11 /app/.venv && \
    chown -R bentoml:bentoml /app/.venv
ENV VIRTUAL_ENV=/app/.venv
ENV UV_COMPILE_BYTECODE=1
RUN uv pip install vllm==0.7.3 ; exit 0
COPY --chown=bentoml:bentoml ./env/python ./env/python/
# install python packages
RUN uv pip install -r ./env/python/requirements.txt

RUN uv pip install --compile-bytecode flashinfer-python --find-links https://flashinfer.ai/whl/cu124/torch2.5

COPY --chown=bentoml:bentoml . ./

# Block SETUP_BENTO_ENTRYPOINT
# Default port for BentoServer
EXPOSE 3000

# Expose Prometheus port
EXPOSE 3001

RUN chmod +x /home/bentoml/bento/env/docker/entrypoint.sh

USER bentoml

ENTRYPOINT [ "/home/bentoml/bento/env/docker/entrypoint.sh" ]

