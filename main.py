from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect

import logging
import logger

logging.basicConfig(level=logging.NOTSET)

app = Flask(__name__)
csrf = CsrfProtect(app)
app.config.from_envvar('SETTINGS_FILE')

logger.setup_logging(app)

db = SQLAlchemy(app)
mail = Mail(app)


if __name__ == "__main__":
    app.run()

