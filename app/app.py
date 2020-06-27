# TODO https://github.com/flasgger/flasgger

from flask import Flask, request
from flask_restful import Resource, Api
from config import Config
from extensions import db, jwt
from flask_migrate import Migrate
from flask_cors import CORS
from resources.user import UserResource
from resources.test import ApiTestResource
from resources.token import (
        TokenResource,
        RevokeTokenResource,
        black_list
    )
from resources.test_auth import ApiTestAuthResource
from resources.item import ItemResource

def create_app():
    app = Flask(__name__)
    # https://flask-cors.readthedocs.io/en/latest/
    #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    cors = CORS(app)
    app.config.from_object(Config)
    register_extensions(app)
    
    register_basic_resources(app)
    register_app_specific_resources(app)
    
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in black_list

def register_basic_resources(app):
    # TODO refresh token
    # TODO test revoke
    api = Api(app)
    api.add_resource(UserResource, '/api/v1' + '/users')
    api.add_resource(ApiTestResource, '/api/v1' + '/status')
    api.add_resource(TokenResource,'/api/v1'+ '/auth')
    api.add_resource(RevokeTokenResource,'/api/v1'+ '/auth')
    api.add_resource(ApiTestAuthResource,'/api/v1'+ '/auth_test')

def register_app_specific_resources(app):
    api = Api(app)
    api.add_resource(ItemResource,'/api/v1'+ '/items')

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=5000)
