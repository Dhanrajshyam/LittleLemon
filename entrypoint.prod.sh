#!/usr/bin/env bash
set -e  # Exit on any error

echo "Running Django migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn Littlelemon.wsgi:application --bind 0.0.0.0:8000 --workers 3
