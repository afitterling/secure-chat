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

        # https://www.base64encode.org/
        
        SECRET_KEY = 'VmllbGUgZWluc2lsYmlnZSBlbmdsaXNjaGUgTm9tZW4gc2luZCBOb21pbmFsaXNpZXJ1bmdlbiB2b24gVmVyYmVuOyBzaWUgd2VyZGVuIHdpZSBlbnRzcHJlY2hlbmRlIGRldXRzY2hlIEJpbGR1bmdlbiAoZGVyIExhdWYvU3BydW5nOyAKCkhvYmVyZywgUnVkb2xmLEhvYmVyZywgVXJzdWxhLiBEZXV0c2NoZSBHcmFtbWF0aWsgKFNBICJ0byBnbyIpOiBFaW5lIFNwcmFjaGxlaHJlIGbDvHIgQmVydWYsIFN0dWRpdW0sIEZvcnRiaWxkdW5nIHVuZCBBbGx0YWc6IEVpbmUgU3ByYWNobGVocmUgZsO8ciBCZXJ1ZiwgU3R1ZGl1bSwgRm9ydGJpbGR1bmcgdW5kIEFsbHRhZyAoRGVyIGtsZWluZSBEdWRlbikgKEdlcm1hbiBFZGl0aW9uKSAoS2luZGxlLVBvc2l0aW9uZW40NTczLTQ1NzQpLiBEdWRlbi4gS2luZGxlLVZlcnNpb24uIA=='\
                if not os.environ.get('SECRET_KEY') else os.environ.get('SECRET_KEY')
        #SECRET_KEY = os.environ.get('SECRET_KEY')
        
        JWT_ERROR_MESSAGE_KEY = 'message'

        JWT_BLACKLIST_ENABLED = True
        JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
        

