#!/bin/bash

echo "Checking if Docker is running..."
{ docker info >/dev/null 2>&1; echo "Docker OK"; } || { echo "Docker is required and does not seem to be running - please start Docker and retry" ; exit 1; }

docker build -t impala-autoscale:latest .
docker run -it --name impala-autoscale impala-autoscale