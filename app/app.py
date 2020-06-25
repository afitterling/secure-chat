from flask import Flask, request
from flask_restful import Resource, Api
from config import Config
from extensions import db
from flask_migrate import Migrate

from resources.user import UserResource
from resources.test import ApiTestResource

#TODO
#https://flask-cors.readthedocs.io/en/latest/

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)

def register_resources(app):
    api = Api(app)
    api.add_resource(UserResource, '/api/v1' + '/users')
    api.add_resource(ApiTestResource, '/api/v1' + '/status')

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=5000)
