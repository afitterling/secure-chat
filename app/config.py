import os

class Config:
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dbuser:dbpasswd@postgres/appdb'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        # https://stackoverflow.com/questions/56271116/flask-sqlalchemy-sqlalchemy-engine-options-not-set-up-correctly
        #SQLALCHEMY_POOL_RECYCLE = 3600
        SQLALCHEMY_ENGINE_OPTIONS = {
                'pool_recycle': 3600,
                'pool_pre_ping': True
        }

        SECRET_KEY = os.environ.get('SECRET_KEY')
        
        JWT_ERROR_MESSAGE_KEY = 'message'
        JWT_BLACKLIST_ENABLED = True
        JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
        

