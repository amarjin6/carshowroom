#!/bin/bash

python3 manage.py collectstatic --noinput
python3 manage.py migrate
gunicorn showroom.wsgi:application --bind 0.0.0.0:8000

