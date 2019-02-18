from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   # Getting popular movie
    popular_source = get_source('popular')
    print(popular_source)
    title = 'Home - Welcome to The best Source Review Website Online'
    return render_template('index.html', title = title,popular = popular_source)

@app.route('/source/<source_id>')
def source(source_article):

    '''
    View source page function that returns the source details page and its data
    '''

    title = 'Home - Welcome to The best News Source Review Website Online'
    return render_template('source.html', title = title)

    return render_template('source.html',article = source_article) 

