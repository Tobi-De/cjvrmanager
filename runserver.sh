#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn cjvrmanager.wsgi --bind=0.0.0.0:80