from flask import Flask, request
from flask_restful import Resource, Api
from config import Config
from extensions import db
from flask_migrate import Migrate

from resources.user import UserListResource
from models.user import User

#, request
#from flask_restful import Resource, Api
#from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    #api = Api(app)

    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)

    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    api = Api(app)

    api.add_resource(UserListResource, '/api/v1' + '/users')


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=5000)
