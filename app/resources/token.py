from http import HTTPStatus
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from utils import verify_password
from models.user import User

