#!/bin/bash

# Variables
DOCKER_IMAGE_NAME="mlops-skeleton-project"
DOCKER_REGISTRY="your_docker_registry"  # Replace with your Docker registry
DOCKER_TAG="latest"

# Build Docker images
echo "Building Docker images..."
docker build -t $DOCKER_IMAGE_NAME:training -f docker/Dockerfile.training .
docker build -t $DOCKER_IMAGE_NAME:serving -f docker/Dockerfile.serving .

# Tag Docker images
echo "Tagging Docker images..."
docker tag $DOCKER_IMAGE_NAME:training $DOCKER_REGISTRY/$DOCKER_IMAGE_NAME:training-$DOCKER_TAG
docker tag $DOCKER_IMAGE_NAME:serving $DOCKER_REGISTRY/$DOCKER_IMAGE_NAME:serving-$DOCKER_TAG

# Push Docker images to registry
echo "Pushing Docker images to registry..."
docker push $DOCKER_REGISTRY/$DOCKER_IMAGE_NAME:training-$DOCKER_TAG
docker push $DOCKER_REGISTRY/$DOCKER_IMAGE_NAME:serving-$DOCKER_TAG

echo "Docker images built and pushed successfully."