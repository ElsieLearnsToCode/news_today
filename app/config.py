# class Config:
#     '''
#     General configuration parent class
#     '''
#     pass


import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

    ARTICLES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    @staticmethod
    def __init__app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True




