FROM python:3.8-slim-buster

RUN mkdir -p /app
RUN mkdir -p /usr/src/static
RUN mkdir -p /usr/src/data

WORKDIR /app
COPY ./ /app

RUN pip install -r requirements.txt