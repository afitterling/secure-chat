from models.user import User
from models.item import Item
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request
from http import HTTPStatus
from flask_restful import Resource

class ItemResource(Resource):

    @jwt_required
    def post(self):
        user = User.get_by_id(id=get_jwt_identity())
        
        if not user:
            return HTTPStatus.FORBIDDEN

        json_data = request.get_json()
        item_name = json_data.get('name')

        item = Item(user_id=user.id, name=item_name)
        
        item.save()
        
        data = {'id': item.id, 'name': item.name}

        return data, HTTPStatus.OK



