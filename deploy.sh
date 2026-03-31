#!/bin/bash
# Variables
IMAGE_NAME="devops-app"
CONTAINER_NAME="devops-container"
PORT=${1:-5000}

# Stop ancien container
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Build image
docker build -t $IMAGE_NAME .

# Run container
docker run -d -p $PORT:5000 --name $CONTAINER_NAME $IMAGE_NAME

# Messages
echo "App déployée sur localhost:$PORT"
echo "Déploiement terminé"
