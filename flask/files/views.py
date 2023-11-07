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
from .models import get_info_concert

@app.route("/")
def home():
    return render_template("home.html", title="Home")


@app.route("/asso/bien-etre")
@login_required
def accueil_bien_etre():
    return render_template("accueil_bien_etre.html") 

@app.route("/asso/technique")
@login_required
def accueil_technique():
    return render_template("accueil_technique.html")    

class LoginForm(FlaskForm):
    nomOrga = StringField('Username')
    motDePasse = PasswordField('Password')
    next = HiddenField()
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
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            if user.typeOrga == "Technique":
                login_user(user)
                return redirect(url_for("accueil_technique"))
            else:
                login_user(user)
                return redirect(url_for("accueil_bien_etre"))
    return render_template("connexion.html", form=f)

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('connexion'))

@app.route("/choix_fiche/", methods = ("GET","POST",))
def choix_fiche():
    return render_template("choix_fiche.html")

@app.route("/creation_concert")
def creation_concert():
    return render_template("creation_concert.html")

@app.route("/liste_concerts/", methods = ("GET","POST",))
def liste_concerts():
    return render_template("liste_concerts.html",title="Les Concerts",concerts=get_info_concert())