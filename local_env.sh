#!/bin/sh
# nginx -g daemon off; -c /etc/nginx/nginx.conf;
# uwsgi --http :80 --module sanka.wsgi --py-autoreload 1;
python manage.py runserver 8000;