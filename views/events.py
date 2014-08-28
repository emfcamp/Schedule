from main import app, db
from views import Form
from models.event import Event, EventFavourite

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

from flask import (
    render_template, redirect, request, flash,
    url_for, _request_ctx_stack, jsonify
)
from flask.ext.login import (
    login_user, login_required, logout_user, current_user,
)

from wtforms.validators import Required
from wtforms import TextField, PasswordField, HiddenField

import re

class EventFavouriteForm(Form):
    pass


@app.route('/events', methods=['GET'])
def events():
    form = EventFavouriteForm()
    events = Event.query.order_by(Event.location_id, Event.start_time).all()
    return render_template("events.html", events=events, form=form)

@app.route('/events/<id>/favourite', methods=['POST'])
@login_required
def add_favourite(id):
    event = Event.query.get(id)
    if event is not None and event not in current_user.events:
        current_user.events.append(event)
        db.session.commit()
    return jsonify(favourite=event in current_user.events, event_id=event.id)

@app.route('/events/<id>/unfavourite', methods=['POST'])
@login_required
def remove_favourite(id):
    event = Event.query.get(id)
    if event is not None and event in current_user.events:
        EventFavourite.query.filter_by(event_id=event.id, user_id=current_user.id).delete()
        db.session.commit()
    return jsonify(favourite=event in current_user.events, event_id=event.id)
