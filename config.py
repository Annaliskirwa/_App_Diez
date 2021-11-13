import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://annalis:Ann123@localhost/quotes'

    pass
class ProdConfig(Config):
        pass
class DevConfig(Config):
        pass


config_options = {
'development': DevConfig,
'production': ProdConfig
}