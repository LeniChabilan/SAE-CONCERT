from flask import Flask
from flask_bootstrap import Bootstrap5
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

def mkpath(p):
    return os.path. normpath (
        os.path.join(
            os.path.dirname(__file__),
            p))

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../../creaConcert.db'))
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "4d166f5f-fa64-461b-878d-d7077d4ef1a2"

login_manager.login_view = "connexion"