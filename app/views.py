from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   # Getting popular article
   # Getting popular article
    popular_article = get_article('popular')
    upcoming_article = get_article('upcoming')
    now_showing_article = get_article('now_playing')
    title = 'Home - Welcome to The best article Review Website Online'
    return render_template('index.html', title = title, popular = popular_article, upcoming = upcoming_article, now_showing = now_showing_article )

@app.route('/article/<article_id>')
def article(article_article):

    '''
    View article page function that returns the article details page and its data
    '''

    title = 'Home - Welcome to The best News article Review Website Online'
    return render_template('article.html', title = title)

    return render_template('article.html',article = article_article) 

