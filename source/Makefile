PWD := $(shell pwd)

BENTOML_HOME := $(PWD)/../bentoml

.PHONY: all
all:
	@rm -rf $(BENTOML_HOME)
	@mkdir -p $(BENTOML_HOME)
	@BENTOML_HOME=$(BENTOML_HOME) python make.py
