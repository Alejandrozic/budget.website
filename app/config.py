import os
import secrets
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(basedir), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_urlsafe()


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    SESSION_COOKIE_SECURE = True
    REMEMBER_SESSION_COOKIE = True
