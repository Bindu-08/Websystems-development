from datetime import datetime

from app.db import db
from flask_login import UserMixin
from flask import current_app
from sqlalchemy.orm import relationship


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    about = db.Column(db.String(300), nullable=True, unique=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column('registered_on', db.DateTime)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    is_admin = db.Column('is_admin', db.Boolean(), nullable=False, server_default='0')
    songs = db.relationship("Song", back_populates="user", cascade="all, delete")

    # `roles` and `groups` are reserved words that *must* be defined
    # on the `User` model to use group- or role-based authorization.

    def __init__(self, email, password):
        self.email = email
        self.password = self.set_password(password)
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def set_password(self, password):
        with current_app.app_context():
            from app import bcrypt

            return bcrypt.generate_password_hash(password.encode('utf-8'))

    def check_password(self, password):
        with current_app.app_context():
            from app import bcrypt

            return bcrypt.check_password_hash(self.password, password.encode('utf-8'))

    def __repr__(self):
        return '<User %r>' % self.email


class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=True, unique=False)
    artist = db.Column(db.String(300), nullable=True, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship("User", back_populates="songs", uselist=False)

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
