from app import app
import urllib.request,json
from .models import article

ARTICLE = article.ARTICLE

# Getting api key
api_key = app.config['ARTICLE_API_KEY']
print(api_key)

# Getting the movie base url
base_url = app.config["ARTICLE_API_BASE_URL"]
print(base_url)

def get_article(category):
    '''
    Function that gets the json response to our url request
    '''
    get__url = base_url.format(category,api_key)
    print(get__url)

    with urllib.request.urlopen(get__url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        print(get_article_response)
        article_results = None

        if get_article_response['results']:
            article_results_list = get_article_response['results']
            article_results = process_results(article_results_list)

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
        articles = article_item.get('articles ')
        title = article_item.get('title ')
        name = article_item.get('name')
        author = article_item.get('author')
        description = article_item.get('description ')
        url = article_item.get('url ')
        publishedAt = publishedAt_item.get('publishedAt')

        if poster:
            article_object = article((articles,title,name,author,description,url))
            article_results.append(article_object)

    return article_results
    