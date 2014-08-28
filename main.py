from flask import Flask
from flask.ext.mail import Mail
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect

import filters
import logging
import logger

logging.basicConfig(level=logging.NOTSET)

app = Flask(__name__)
csrf = CsrfProtect(app)
app.config.from_envvar('SETTINGS_FILE')
app.jinja_env.filters['day_sort'] = filters.day_sort

logger.setup_logging(app)

db = SQLAlchemy(app)
mail = Mail(app)
login_manager = LoginManager()

from views import *
from models import *

if __name__ == "__main__":
    app.run()

