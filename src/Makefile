PWD := $(shell pwd)

BENTOML_HOME := $(PWD)/../bentoml

.PHONY: all
all:
	@BENTOML_HOME=$(BENTOML_HOME) uv run make.py --workers 1
