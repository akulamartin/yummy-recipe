# app/__init__.py

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

# Initialize the app
app = Flask(__name__)


# Load the views
from app import views

app.config['SECRET_KEY'] = 'rukatubanjukatu'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
app.debug = True

toolbar = DebugToolbarExtension(app)
