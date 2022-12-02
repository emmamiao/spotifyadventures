import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('app', __name__, url_prefix='/', static_folder='static')

@bp.route("sentencer", methods=["GET", "POST"])
def sentencer():
    '''creates the sentences.'''
    if request.method == "GET":
        return render_template("sentencer.html")