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
   
    popular_new_article = get_source('popular_news')
    current_news_article = get_source('description_news')
    country_showing_article = get_source('country_location')
  
    title = 'Home - Welcome to The best article Review Website Online'
    return render_template('index.html', title = title, popular_news= popular_new_article, current_news = current_news_article , country_showing= country_showing_article )

@app.route('/article/<article_id>')
def article(article_article):

    '''
    View article page function that returns the article details page and its data
    '''

    title = 'Home - Welcome to The best News article Review Website Online'
    # return render_template('article.html', title = title)

    return render_template('article.html',article = article_article) 

