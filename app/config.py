import os


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///eye.db"
    Debug = True


class DevelopmentConfig(BaseConfig):
    Debug = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///eye.db"


class ProductionConfig(BaseConfig):
    Debug = False


class TestingConfig(BaseConfig):
    Debug = True
    Testing = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
