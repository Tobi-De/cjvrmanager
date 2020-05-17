FROM python:3.8-slim-buster

RUN mkdir -p /app
RUN mkdir -p /usr/src/static
RUN mkdir -p /usr/src/data

WORKDIR /app
COPY ./ /app

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  && apt-get install postgresql-contrib \
  && apt-get install gcc \
  && apt-get install python3-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt