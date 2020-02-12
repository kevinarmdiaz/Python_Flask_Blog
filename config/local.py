# config/local.py
from .default import *

APP_ENV = APP_ENV_LOCAL

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/miniblog'