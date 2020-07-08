from models.user import User
from models.item import Item
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request, jsonify, Response
from http import HTTPStatus
from flask_restful import Resource
from messages import *
from extensions import redis

def event_stream(channel_name):
    pubsub = redis.pubsub()
    pubsub.subscribe('topic-' + channel_name)
    # TODO: handle client disconnection.
    for message in pubsub.listen():
        print(message)
        if message['type']=='message':
            #r = 'event: message\n%s\n\n' % message['data'].decode('utf-8')
            cm = message['data'].decode('utf-8')
            r = "\n\nevent: message\ndata: "+cm+"\n\n"
            yield r

class ChannelResource(Resource):

    def get(self, channel_name):
        resp = Response(event_stream(channel_name),
                          mimetype="text/event-stream")
        resp.headers['Cache-control'] = 'no-cache'
        resp.headers['X-Accel-Buffering'] = 'no'
        resp.headers['Access-Control-Allow-Credentials'] = 'true'
        return resp

    #@jwt_required
    def post(self, channel_name):
        #user = User.get_by_id(id=get_jwt_identity())
        
        #if not user:
        #    return HTTPStatus.FORBIDDEN

        json_data = request.get_json()
        message = json_data.get('message')

        # TODO attack protection
        nsubs = redis.publish('topic-' + channel_name, str(message))
        
        return {'nsubs': nsubs}, HTTPStatus.OK

