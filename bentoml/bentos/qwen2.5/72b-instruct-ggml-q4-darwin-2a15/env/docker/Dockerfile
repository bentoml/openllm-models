# ===========================================
#
# THIS IS A GENERATED DOCKERFILE. DO NOT EDIT
#
# ===========================================

# Block SETUP_BENTO_BASE_IMAGE
FROM python:3.9-slim AS base-container

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

ARG CMAKE_ARGS=-DGGML_METAL=on
ENV CMAKE_ARGS=$CMAKE_ARGS

RUN mkdir $BENTO_PATH && chown bentoml:bentoml $BENTO_PATH -R
WORKDIR $BENTO_PATH

RUN apt-get update && apt-get install -q -y --no-install-recommends --allow-remove-essential ca-certificates gnupg2 bash build-essential git

RUN pip install uv && UV_PYTHON_INSTALL_DIR=/app/python/ uv venv --python 3.9 /app/.venv
ENV VIRTUAL_ENV=/app/.venv
COPY --chown=bentoml:bentoml ./env/python ./env/python/
# install python packages
RUN uv pip install -r ./env/python/requirements.txt


COPY --chown=bentoml:bentoml . ./

# Block SETUP_BENTO_ENTRYPOINT
# Default port for BentoServer
EXPOSE 3000

# Expose Prometheus port
EXPOSE 3001

RUN chmod +x /home/bentoml/bento/env/docker/entrypoint.sh
RUN chown bentoml:bentoml -R $VIRTUAL_ENV

USER bentoml

ENTRYPOINT [ "/home/bentoml/bento/env/docker/entrypoint.sh" ]

