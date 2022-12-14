import os


from flask import Flask, render_template
from webapp.database import init_db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'adventure.db'),
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/adventures.db'

    db = SQLAlchemy(app)
    db.app = app

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

@db.route('sentencer')
def index():
    return render_template("index.html")

