from main import db
from flask.ext.login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy
import bcrypt
import os
import base64
from datetime import datetime, timedelta


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    badgeid = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    name = db.Column(db.String(10), nullable=True)
    nickname = db.Column(db.String(10), nullable=True)

    events = association_proxy('event_favourites', 'event')

    def __init__(self, email):
        self.email = email

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    def check_password(self, password):
        password = password.encode('utf8')
        password_hash = self.password.encode('ascii')
        return bcrypt.hashpw(password, password_hash) == password_hash


class PasswordReset(db.Model):
    __tablename__ = 'password_reset'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    expires = db.Column(db.DateTime, nullable=False)
    token = db.Column(db.String, nullable=False)

    def __init__(self, email):
        self.email = email
        self.expires = datetime.utcnow() + timedelta(days=1)

    def new_token(self):
        self.token = base64.urlsafe_b64encode(os.urandom(5 * 3))

    def expired(self):
        return self.expires < datetime.utcnow()
