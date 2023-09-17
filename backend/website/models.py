from . import db
from flask_login import UserMixin
from datetime import datetime


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    original_url = db.Column(db.String(255))
    shortened_url = db.Column(db.String(255))
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Shortened Link: {self.shortened_url}"
    
    def __init__(self,)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
