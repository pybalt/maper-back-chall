#!/bin/sh

cd /app/app

echo "Running entrypoint.sh"
python manage.py makemigrations machine metrics sensors
python manage.py migrate machine metrics sensors
python manage.py load_data
python manage.py runserver 0.0.0.0:8000