from flask import render_template
from app import app
from ..request import get_news_sources, get_news_articles
from ..models import Sources, Articles


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_sources = get_news_sources('business')
    sports_sources = get_news_sources('sports')
    technology_sources = get_news_sources('technology')
    entertainment_sources = get_news_sources('entertainment')
    title = 'News Today'
    return render_template('index.html', title = title, business_sources = business_sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@app.route('/sources/<id>')
def sources(id):

    '''
    View sources/articles function that returns the sources page and its data
    '''
    articles = get_news_articles(id)
    title = f'NH | {id}'

    return render_template('sources.html',id = id, title= title,articles = articles)