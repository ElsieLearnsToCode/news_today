from app import app
import urllib.request,json
from app.models import Sources, Articles
from datetime import datetime

# Getting api key
# api_key = app.config['NEWS_API_KEY']
api_key = None

# Getting the news base url
# base_url = app.config["NEWS_API_BASE_URL"]
base_url = None

#getting the articles url
articles_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_news_sources_url = base_url.format(category, api_key)
    
    with urllib.request.urlopen(get_news_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        news_sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)

	return news_sources_results


