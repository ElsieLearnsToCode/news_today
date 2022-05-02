from flask import Flask
from app.config import DevConfig



# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from .main import views