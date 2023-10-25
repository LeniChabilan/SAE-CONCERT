from .app import app
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField
from wtforms.validators import DataRequired
from flask import url_for, redirect

@app.route("/")
def home():
    return render_template("home.html", title="Home")


