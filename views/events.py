from main import app, db
from views import Form
from models.event import Event

from sqlalchemy.exc import IntegrityError

from flask import (
    render_template, redirect, request, flash,
    url_for, _request_ctx_stack
)
from flask.ext.login import (
    login_user, login_required, logout_user, current_user,
)

import re

@app.route('/events', methods=['GET'])
def events():
    events = Event.query.all()
    return render_template("events.html", events=events)



