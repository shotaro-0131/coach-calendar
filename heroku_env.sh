#!/bin/sh
python manage.py migrate; 
gunicorn --bind 0.0.0.0:$PORT sanka.wsgi; 