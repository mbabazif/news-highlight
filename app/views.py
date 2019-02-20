from flask import render_template
from app import app
from .request import get_article
from .request import get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   
   # Getting popular article
    current_source = get_source('everything')
   
    # popular_new_article = get_source('popular_news')
    # current_news_article = get_source('description_news')
    # country_showing_article = get_source('country_location')
  
    title = 'Home - Welcome to The best article Review Website Online'
    return render_template('index.html', title = title, popular_news= popular_news, current_news = current_news_ , country_showing= country_showing )

@app.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(id)
    title = f'{id}'
    title = 'Home - Welcome to The best News article Review Website Online'
    # return render_template('article.html', title = title)

    return render_template('article.html',article = article) 

