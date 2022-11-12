import os
from dotenv import load_dotenv
from envs import env

# до среды, как сослаться на flask.app в качестве стартового конфига
# как устанавливать в venv переменные среды
# какие параметры принимает flask db migrate
# как работать с python console
# как забирать app contex, который ужо стартовал

load_dotenv()


class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_dev_default")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_test_default")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_prod_default")


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

# вынести конфиги
