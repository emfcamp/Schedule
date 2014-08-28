from main import app, db, login_manager

from views import Form
from models.user import User

from flask import (
    render_template, send_from_directory, redirect
)

from flask.ext.login import (
    login_user, login_required, logout_user, current_user,
)

from wtforms.validators import Required, Email, EqualTo, ValidationError, Length
from wtforms import TextField, PasswordField, HiddenField

import os
import re

login_manager.setup_app(app, add_context_processor=True)

@login_manager.user_loader
def load_user(userid):
    user = User.query.filter_by(id=userid).first()
    _request_ctx_stack.top.badgeid = user.badgeid
    return user

@app.route('/')
def main():
    if current_user.is_authenticated():
        return redirect("/home", code=302)
    else:
        return redirect("/events", code=302)

def Validate_Badge_ID(form, field):
    if field.data:
        if len(field.data) != 7:
            raise ValidationError('Badge IDs are 7 Characters')
        if not re.match(r"[eE][mM][fF][0-9A-Fa-f]{4}", field.data):
            raise ValidationError('Badge IDs begin EMF then have 4 numbers / letters')

class HomeForm(Form):
    badgeid = TextField('Badge ID', [Validate_Badge_ID])
    phone = TextField('Mobile phone number', [])
    name = TextField('Your Name', [Length(max=10)])
    nickname = TextField('Your NickName', [Length(max=10)])


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = HomeForm()

    user = User.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        user.name = form.name.data
        user.nickname = form.nickname.data
        user.badgeid = form.badgeid.data.upper()
        user.phone = form.phone.data
        db.session.commit()

    form.name.data = user.name
    form.nickname.data = user.nickname
    form.phone.data = user.phone
    form.badgeid.data = user.badgeid

    return render_template("home.html", user=current_user, form=form)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

