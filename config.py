import os

class Config:
    pass
class ProdConfig(Config):
        pass
class DevConfig(Config):
        pass


config_options = {
'development': DevConfig,
'production': ProdConfig
}