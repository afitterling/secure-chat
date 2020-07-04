from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager
)
from redis import Redis

db = SQLAlchemy()
jwt = JWTManager()
redis = Redis(host='redis', port=6379)
