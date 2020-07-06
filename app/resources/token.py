from redis import Redis
from http import HTTPStatus
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt
    )
    
from extensions import jwt
from utils import verify_password
from models.user import User

redis = Redis(host='redis', port=6379)

def black_list_add(jti):
    redis.sadd('black_list', jti)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return redis.sismember('black_list', jti)


class TokenResource(Resource):

    def post(self):
        json_data = request.get_json()
        email = json_data.get('email')
        password = json_data.get('password')
        
        user = User.get_by_email(email=email)

        if not user or not verify_password(password, user.password):
            return {'message': 'email or password is incorrect'}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=user.id, fresh=True)

        refresh_token = create_refresh_token(identity=user.id)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
            }, HTTPStatus.OK

class RevokeTokenResource(Resource):

    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        #black_list.add(jti)        
        black_list_add(jti)
        return {'message': 'Successfully logged out'}, HTTPStatus.OK


class RefreshTokenResource(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user,fresh=False)
        return {access_token: access_token}, HTTPStatus.OK

