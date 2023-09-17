import random
import string
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'radadadadaadadadaddad'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Md2072121@localhost/UrlLinkShortener'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
