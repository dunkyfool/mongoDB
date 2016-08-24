#!/bin/sh

docker network ls
docker network create my-mongo-cluster
docker network ls

