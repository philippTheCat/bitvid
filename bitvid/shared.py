__author__ = 'pharno'

import base64
from uuid import uuid4
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request
from functools import wraps

from errors import LoginRequiredException
db = SQLAlchemy()

def generate_token():
    return str(uuid4())

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.session.user is None:
            raise LoginRequiredException()
        return f(*args, **kwargs)
    return decorated_function