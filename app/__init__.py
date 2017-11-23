"""The application is initialized here"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
#Initialize the application
APP = Flask(__name__)

# the toolbar is only enabled in debug mode:
APP.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
APP.config['SECRET_KEY'] = 'drums are 808'
APP.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
TOOLBAR = DebugToolbarExtension(APP)

#Load the views
from app import views
