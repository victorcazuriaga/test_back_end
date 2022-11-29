FROM python:3.10

ENV DOCKER_DEFAULT_PLATFORM=linux/amd64

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install -U pip
RUN pip install -r requirements.txt