from main import app

from flask_wtf import Form as BaseForm

class Form(BaseForm):
    # CsrfProtect limit
    TIME_LIMIT = 3600 * 24


import basic  # noqa
import users  # noqa
import events
