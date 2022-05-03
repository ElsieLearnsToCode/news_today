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




