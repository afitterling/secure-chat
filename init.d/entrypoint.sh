#!/bin/sh
cd app
python3 -m flask db upgrade
gunicorn "app:create_app()" -k gevent -b 0.0.0.0:8000
