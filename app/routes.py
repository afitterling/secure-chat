from flask_restful import Api
from resources.user import (UserResource)
from resources.test import ApiTestResource
from resources.token import TokenResource, RefreshTokenResource, RevokeTokenResource
from resources.test_auth import ApiTestAuthResource
from resources.item import (
    ItemListResource,
    ItemResource
)

def register_basic_resources(app):
    api = Api(app)
    api.add_resource(UserResource, '/api/v1' + '/users')
    api.add_resource(ApiTestResource, '/api/v1' + '/status')
    api.add_resource(TokenResource,'/api/v1'+ '/auth')
    api.add_resource(RefreshTokenResource,'/api/v1'+ '/refresh')
    api.add_resource(RevokeTokenResource,'/api/v1'+ '/revoke')
    api.add_resource(ApiTestAuthResource,'/api/v1'+ '/auth_test')

def register_app_specific_resources(app):
    api = Api(app)
    api.add_resource(ItemListResource,'/api/v1/'+ 'items', methods = ['GET', 'POST'])
    api.add_resource(ItemResource,'/api/v1/'+ 'items/<int:id>', methods = ['DELETE', 'PUT'])

