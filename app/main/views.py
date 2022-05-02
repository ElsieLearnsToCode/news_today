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

@app.route('/sources/<id>')
def sources(id):

    '''
    View sources/articles function that returns the sources page and its data
    '''
    return render_template('sources.html',id = id)