cd app
gunicorn "app:create_app()" -k gevent -b 0.0.0.0:8000

