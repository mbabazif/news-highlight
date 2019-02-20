from app import app
import urllib.request,json
from .models import article
from .models import source

ARTICLE = article.ARTICLE
SOURCE = source.SOURCE
# Getting api key
api_key = app.config['ARTICLE_API_KEY']
api_key = app.config['SOURCE_API_KEY']
# print(api_key)

# Getting the api article url
base_url = app.config["ARTICLE_API_BASE_URL"]
base_url = app.config["SOURCE_API_BASE_URL"]
# print(base_url)


def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get__url = base_url.format(api_key)
    print(get__url)

    with urllib.request.urlopen(get__url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)
    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        
        
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description ')
        country = source_item.get('country ')
        source_object = SOURCE(id,name,description,country)
        source_results.append(source_object) 
    return source_results    

def get_article(id):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = article_base_url.format(id,api_key)
    

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        # print(get_article_response)
        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)
    
    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        
        
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title ')
        description = article_item.get('description ')
        url = article_item.get('url ')
        urlToImage = article_item.get('urlToImage ')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content ')

        if urlToImage:
            article_object = article((name,author,title,description,url,urlToImage,publishedAt,content))
            article_results.append(article_object)   

    return article_results
    