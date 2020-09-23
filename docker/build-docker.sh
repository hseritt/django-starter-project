#!/usr/bin/env bash

# See https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
./teardown-docker.sh
pip-review --auto
pip freeze > ../requirements.txt
cp ../requirements.txt .
./pkg-dist.sh
docker-compose build
docker-compose up -d --build
docker-compose exec web sh resetdb.sh
rm -rf dist/*
docker ps
