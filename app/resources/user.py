from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus

#from utils import hash_password
#from models.user import user

class UserListResource(Resource):
        def get(self):
            return jsonify({'data': []})
