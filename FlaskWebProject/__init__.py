"""
The flask application package.
"""
import os
from logging.handlers import RotatingFileHandler
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
# Create logs folder if it doesn't exist
if not os.path.exists('logs'):
    os.mkdir('logs')

# Setup a rotating file handler
file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setLevel(logging.INFO)

# Define log format
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s [in %(pathname)s:%(lineno)d]'
)
file_handler.setFormatter(formatter)

# Add the handler to the app logger
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Flask app startup')

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
