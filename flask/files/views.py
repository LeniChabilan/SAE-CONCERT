from .app import app, db
from flask import render_template, url_for, redirect
from flask_login import login_user , current_user, logout_user, login_required
from hashlib import sha256
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField, PasswordField
from .models import Organisation, ajouter_concert,  supprimer_concert, get_info_concert, chercher_groupe, mod_concert,  get_info_un_concert
from wtforms.validators import DataRequired
from flask import request

from .models import *




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

@app.route("/choix-fiche/", methods = ("GET","POST",))
def choix_fiche():
    return render_template("choix_fiche.html")

@app.route("/creation_concert")
def creation_concert():
    return render_template("creation_concert.html")


@app.route("/liste_concerts/", methods = ("GET","POST",))
def liste_concerts():
    return render_template("liste_concerts.html",title="Les Concerts",concerts=get_info_concert())

@app.route("/save-concert", methods =["POST"])
def save_concert():
    nom = request.form.get("nom")
    dateD = request.form.get("dateD")
    dateF = request.form.get("dateF")
    ficheTech =request.form.get("fiche")
    catering = request.form.get("catering")
    salle = request.form.get("salle")
    groupe = request.form.get("groupe")
    ajouter_concert(nom, dateD, dateF, ficheTech, catering, salle, groupe)
    return render_template("accueil_bien_etre.html", title="Home")

@app.route("/sup-concert/<int:id>")
def sup_concert(id):
    supprimer_concert(id)
    return render_template("liste_concerts.html",title="Les Concerts", concerts=get_info_concert())


@app.route("/modif-concert/<int:id>", methods =["POST"])
def modif_concert(id):
    nom = request.form.get("nom")
    dateD = request.form.get("dateD")
    dateF = request.form.get("dateF")
    ficheTech =request.form.get("fiche")
    catering = request.form.get("catering")
    salle = request.form.get("salle")
    groupe = request.form.get("groupe")
    mod_concert(id,nom, dateD, dateF, ficheTech, catering, salle, groupe)
    return render_template("liste_concerts.html", title="Les Concerts",concerts=get_info_concert())

@app.route("/modification_concert/<int:id>")
def modification_concert(id):
    return render_template("modifier_concert.html",concert=get_info_un_concert(id), cID=id)

@app.route("/entrer-groupe")
def inscription_groupe():
    return render_template("entrer_groupe.html")

@app.route("/recherche-groupe", methods =["POST"])
def recherche_groupe():
    nom_groupe = request.form.get("nom")
    groupe = chercher_groupe(nom_groupe)
    return redirect(url_for("completer_fiche"))

@app.route("/completer-fiche")
def completer_fiche():
    return render_template("completer_fiche.html")

@app.route("/retour/<string:typeOrga>")
def retour(typeOrga):
    if typeOrga == "Technique":
        return redirect(url_for("accueil_technique"))
    else:
        return redirect(url_for("accueil_bien_etre"))
    

@app.route("/liste_groupes/", methods = ("GET","POST",))
def liste_groupes():
    return render_template("liste_groupes.html",title="Les Groupes",groupes=get_dico_grps())

@app.route("/liste_artistes/", methods = ("GET","POST",))
def liste_artistes():
    return render_template("liste_artiste.html",title="Les Artistes", lArt=get_info_artiste())

@app.route("/choix/<string:typeOrga>")
def choix(typeOrga):
    print(typeOrga)
    if typeOrga == "Technique":
        return redirect(url_for("Consulter_fiches"))
    else:
        return redirect(url_for("choix_fiche"))
    

@app.route("/Consulter_fiches")
def Consulter_fiches():
    return render_template("Consulter_fiches.html")

@app.route("/choix-artiste-groupe/", methods = ("GET","POST",))
def choix_groupes_artistes():
    return render_template("choix_groupes_artistes.html")

@app.route("/visualiser_fiches/", methods = ("GET","POST",))
def visualiser_fiches():
    return render_template("visualisation_fiches.html")