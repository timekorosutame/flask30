import os

# дефолтна конфігурація
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = b't\xb9\x9f\xa7\xc52)mC\x9d#\xa5\xc3c\x9f\xbd\x111\t\xae@w\x93\xd1'
	#SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False

# тестова конфігурація
class DevConfig(BaseConfig):
	DEBUG = True

# робоча конфігурація
class ProdConfig(BaseConfig):
	DEBUG = False
