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
    general_cat = get_source('general')
    sports_cat = get_source('sports')
    business_cat = get_source('business')
    entertainment_cat = get_source('entertainment')
  
    title = 'Home - Welcome to The best article Review Website Online'
    return render_template('index.html', title = title, general= general_cat, sports = sports_cat , entertainment=entertainment_cat)

@app.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''
    articles = get_article(id)
    
    # print(articles)
    title = f'{id}'
    title = 'Home - Welcome to The best News article Review Website Online'
    # return render_template('article.html', title = title)

    return render_template('article.html',id = id, articles = articles) 

