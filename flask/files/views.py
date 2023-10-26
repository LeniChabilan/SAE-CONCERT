from .app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("home.html", title="Home")


@app.route("/asso/bien-etre")
def accueil_bien_etre():
    return render_template("accueil_bien_etre.html")    

@app.route("/connexion")
def connexion():
    return render_template("connexion.html")    