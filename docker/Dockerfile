# pull official base image
FROM python:3.8.5-alpine

# set work directory
WORKDIR /app/django_starter

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk add --update alpine-sdk
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install Python packages
RUN pip install --upgrade pip
COPY requirements.txt /app/django_starter/requirements.txt
RUN pip install --use-feature=fast-deps -r /app/django_starter/requirements.txt

# copy project
COPY dist/. /app/django_starter/.
