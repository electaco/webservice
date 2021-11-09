#!/bin/sh
sleep 2
python manage.py migrate --noinput 
supervisord -c supervisord.conf -n