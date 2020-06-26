from flask import request, jsonify
from flask_restful import Resource
from http import HTTPStatus
from utils import hash_password
from models.user import User

class UserResource(Resource):
        def post(self):
            json_data = request.get_json()

            username = json_data.get('username')
            email = json_data.get('email')
            no_hash_password = json_data.get('password')

            if User.get_by_username(username):
                return {'message': 'username used already'}, HTTPStatus.BAD_REQUEST

            if User.get_by_email(email):
                return {'message': 'email used already'}, HTTPStatus.BAD_REQUEST

            user = User(username=username, email=email, password=hash_password(no_hash_password) )
            user.save()

            data = {'id': user.id, 'username': user.username, 'email': user.email}

            return data, HTTPStatus.CREATED

            
