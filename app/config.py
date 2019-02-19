class Config:
    '''
    General configuration parent class
    '''
    ARTICLE_API_BASE_URL ='https://api.thearticledb.org/3/article/{}?api_key={}'
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources/{}?api_key={}'



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