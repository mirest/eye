import os


class BaseConfig(object):
    Debug = True


class DevelopmentConfig(BaseConfig):
    Debug = True
    CSRF_ENABLED = True


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
