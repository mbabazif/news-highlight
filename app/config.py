class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL ='https://api.thesourcedb.org/3/source/{}?api_key={}'



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