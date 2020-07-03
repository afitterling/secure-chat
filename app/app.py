# TODO https://github.com/flasgger/flasgger

from flask import Flask, request
from flask_restful import Resource
from config import Config
from extensions import db, jwt
from flask_migrate import Migrate
from flask_cors import CORS
#from resources.token import (black_list)
from routes import *

def create_app():
    app = Flask(__name__)
    # https://flask-cors.readthedocs.io/en/latest/
    cors = CORS(app) # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(Config)
    register_extensions(app)
    
    register_basic_resources(app)
    register_app_specific_resources(app)

    list_routes(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

#@jwt.token_in_blacklist_loader
#def check_if_token_in_blacklist(decrypted_token):
#    jti = decrypted_token['jti']
#    return jti in black_list

def list_routes(app):
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append('%s' % rule)
    return routes

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=5000)
