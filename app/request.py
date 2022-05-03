from app import app
import urllib.request,json
from app.models import Sources, Articles
from datetime import datetime

# Getting api key
api_key = app.config['NEWS_API_KEY']



