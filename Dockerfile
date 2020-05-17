FROM tiangolo/meinheld-gunicorn:python3.7-alpine3.8

RUN mkdir -p /app
RUN mkdir -p /usr/src/static
RUN mkdir -p /usr/src/data

WORKDIR /app
COPY ./ /app

RUN apt install postgresql-contrib libpq-dev gcc python3-dev

RUN pip install -r requirements.txt