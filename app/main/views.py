from flask import render_template
from app import app


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Welcome to News Today: Reliable, Timely and Objective'
    return render_template('index.html',message = message)

@app.route('/articles/<id>')
def sources(sources_id):

    '''
    View sources/articles function that returns the articles page and its data
    '''
    return render_template('sources.html',id = sources_id)