SHELL := /bin/bash
.ONESHELL:

# Rasa dir
RASA_DIR := rasa-inference
VENV := ./venv/bin/activate

# Start rasa config
init:
	cd $(RASA_DIR)
	source $(VENV)
	rasa init

# Rasa training
train:
	cd $(RASA_DIR)
	source $(VENV)
	rasa train

# Start rasa inference API
run:
	cd $(RASA_DIR)
	source $(VENV)
	rasa run --enable-api

# Deploy
deploy:
	cd $(RASA_DIR)
	source $(VENV)
	rasa train
	rasa run --enable-api