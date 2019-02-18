from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The  n   News Source Review Website Online'
    return render_template('index.html', title = title)

@app.route('/source/<source_id>')
def source(source_id):

    '''
    View source page function that returns the source details page and its data
    '''

    title = 'Home - Welcome to The best News Source Review Website Online'
    return render_template('source.html', title = title)

    return render_template('source.html',id = source_id) 

