# Define variables
PYTHON = python
MAIN_PY = main.py
DOCKER_IMAGE_NAME = file-processing-system
DOCKERFILE = Dockerfile

# Default target to run the app
run:
	$(PYTHON) $(MAIN_PY)

# Run in Single File Mode
input:
	$(PYTHON) $(MAIN_PY) --input $(file)

# Run in Watch Mode
watch:
	$(PYTHON) $(MAIN_PY) --watch

# Build Docker image
docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) -f $(DOCKERFILE) .

# Run Docker container
docker-run:
	docker run -d -p 5000:5000 --name $(DOCKER_IMAGE_NAME) $(DOCKER_IMAGE_NAME)

# Clean up .pyc files
clean:
	rm -f **/*.pyc

# Clean Docker container and image
docker-clean:
	docker rm -f $(DOCKER_IMAGE_NAME)
	docker rmi $(DOCKER_IMAGE_NAME)
