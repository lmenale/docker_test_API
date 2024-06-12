#!/bin/bash

# Executing the FastAPI image
docker image pull datascientest/fastapi:1.0.0

# Build the images
docker-compose build

# Run the tests
docker-compose up
