from .app import app, db
from flask import render_template, url_for, redirect
from flask_login import login_user , current_user, logout_user, login_required
from hashlib import sha256
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField, PasswordField
from .models import Organisation
from wtforms.validators import DataRequired
from .models import Organisation
from flask import request

@app.route("/")
def home():
    return render_template("home.html", title="Home")


@app.route("/asso/bien-etre")
def accueil_bien_etre():
    return render_template("accueil_bien_etre.html")    

class LoginForm(FlaskForm):
    nomOrga = StringField('Username')
    motDePasse = PasswordField('Password')
    def get_authenticated_user(self):
        user = Organisation.query.get(self.nomOrga.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.motDePasse.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.motDePasse else None

@app.route("/connexion/", methods =("GET","POST",))
def connexion():
    f = LoginForm()
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("accueil_bien_etre"))
    return render_template("connexion.html", form=f)
