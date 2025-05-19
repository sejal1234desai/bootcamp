# Makefile for Figure Caption Extraction and Access System

# Variables
PYTHON=python
VENV_NAME=venv
ACTIVATE=. $(VENV_NAME)/bin/activate
INPUT_FILE=data/sample_ids.txt
ENV_FILE=.env
DOCKER_ENV_FILE=.env_docker
APP_MODULE=app.api:app

# Default target
help:
	@echo "Makefile Usage:"
	@echo "  make setup         - Set up virtual environment and install dependencies"
	@echo "  make run           - Run the FastAPI app using uvicorn"
	@echo "  make ingest        - Ingest papers from sample_ids.txt"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-run    - Run Docker container"
	@echo "  make clean         - Remove virtual environment"
	@echo "  make format        - Format code with black"
	@echo "  make lint          - Run flake8 for linting"

setup:
	uv venv $(VENV_NAME)
	$(ACTIVATE) && pip install -r requirements.txt

run:
	uvicorn $(APP_MODULE) --reload

ingest:
	$(PYTHON) app/ingest.py --input $(INPUT_FILE)

docker-build:
	docker build -t fig_api .

docker-run:
	docker run -d -p 8000:8000 --env-file $(DOCKER_ENV_FILE) fig_api

clean:
	rm -rf $(VENV_NAME)

format:
	black app/

lint:
	flake8 app/
