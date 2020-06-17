class Config:
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dbuser:dbpasswd@postgres/appdb'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        