cd app
gunicorn "app:create_app()" -b 0.0.0.0:5000

