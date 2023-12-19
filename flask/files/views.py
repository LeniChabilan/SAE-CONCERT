from .app import app, db
from flask import render_template, url_for, redirect
from flask_login import login_user , current_user, logout_user, login_required
from hashlib import sha256
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField, PasswordField

from .models import Organisation, Concert

from .requetes import ajouter_concert,  supprimer_concert,supprimer_groupe, get_info_concert, chercher_groupe, mod_concert,  get_info_un_concert, get_liste_salle, get_liste_groupe, get_artiste_groupe, get_info_artiste, get_dico_grps, mod_artiste, mod_artiste, get_info_un_artiste, supprimer_artiste,get_plan_concert, ajouter_artiste

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
    return render_template("creation_concert.html", liste_salle=get_liste_salle(), liste_groupe=get_liste_groupe())


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

@app.route("/modification_concert/<int:id>")
def modification_concert(id):
    return render_template("modifier_concert.html", concert=get_info_un_concert(id), cID=id,liste_salle=get_liste_salle(), liste_groupe=get_liste_groupe())

@app.route("/sup-groupe/<int:id>")
def sup_groupe(id):
    supprimer_groupe(id)
    return render_template("liste_groupes.html",title="Les Groupes",groupes=get_dico_grps())

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

@app.route("/entrer-groupe")
def inscription_groupe():
    return render_template("entrer_groupe.html")

@app.route("/recherche-groupe", methods=['GET', 'POST'])
def recherche_groupe():
    nom_groupe = request.form.get("nom")
    groupe = chercher_groupe(nom_groupe)
    if get_artiste_groupe(groupe.groupeID) == []:
        return render_template("ajout_artiste.html", id = groupe.groupeID)
    return redirect(url_for("completer_fiche"))

@app.route("/completer-fiche", methods=['GET', 'POST'])
def completer_fiche():
    return render_template("completer_fiche.html")

@app.route("/completer-fiche-pdf", methods=['GET', 'POST'])
def completer_fiche_pdf():
    return render_template("completer_fiche_pdf.html")

@app.route("/ajout-artiste/<int:id>", methods=['GET', 'POST'])
def ajout_artiste(id):
    pseudo = request.form.get("pseudo")
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    email = request.form.get("email")
    dateDN =request.form.get("dateDN")
    lDN = request.form.get("lDN")
    adresse = request.form.get("adresse")
    numSec = request.form.get("numSec")
    numCNI = request.form.get("numCNI")
    dateDelivrance = request.form.get("dateDelivrance")
    dateExpiration = request.form.get("dateExpiration")
    idGroupe = request.form.get("idGroupe")
    ajouter_artiste(pseudo, nom, prenom, email, dateDN, lDN, adresse, numSec, numCNI, dateDelivrance, dateExpiration, idGroupe)
    return render_template("ajout_artiste.html", id = id)

@app.route("/liste_groupes/", methods = ("GET","POST",))
def liste_groupes():
    return render_template("liste_groupes.html",title="Les Groupes",groupes=get_dico_grps())

@app.route("/liste_artistes/", methods = ("GET","POST",))
def liste_artistes():
    return render_template("liste_artiste.html",title="Les Artistes", lArt=get_info_artiste())

@app.route("/choix/<string:typeOrga>/<int:concert>", methods = ("GET","POST"))
def choix(typeOrga,concert):
    if typeOrga == "Technique":
        return render_template("Consulter_fiches.html",conc=get_info_un_concert(concert))
    else:
        return render_template("choix_fiche.html",conc=get_info_un_concert(concert))
    

@app.route("/Consulter_fiches")
def Consulter_fiches():
    return render_template("Consulter_fiches.html")

@app.route("/choix-artiste-groupe/", methods = ("GET","POST",))
def choix_groupes_artistes():
    return render_template("choix_groupes_artistes.html")

@app.route("/visualiser_fiches/<int:conc>", methods = ("GET","POST",))
def visualiser_fiches(conc):
    return render_template("visualisation_fiches.html",conc=get_info_un_concert(conc))

@app.route("/visualiser_plan/<int:conc>", methods = ("GET","POST",))
def visualiser_plan(conc):
    concert=get_info_un_concert(conc)
    return render_template("visualisation_plan.html",plan=get_plan_concert(concert.salleID),conc=concert)


@app.route("/sup-artiste/<int:id>")
def sup_artiste(id):
    supprimer_artiste(id)
    return render_template("liste_artiste.html",title="Les Artistes", lArt=get_info_artiste())


@app.route("/sup-artiste-grp/<int:id>")
def sup_artiste_grp(id):
    supprimer_artiste(id)
    return render_template("liste_groupes.html",title="Les Groupes",groupes=get_dico_grps())

@app.route("/modification_artiste/<int:id>")
def modification_artiste_art(id):
    return render_template("modifier_artiste_art.html", arti=get_info_un_artiste(id), aID=id)

@app.route("/modification_artiste_grp/<int:id>")
def modification_artiste_grp(id):
    return render_template("modifier_artiste_grp.html", arti=get_info_un_artiste(id), aID=id)

@app.route("/modif-artiste-art/<int:id>", methods =["POST"])
def modif_artiste_art(id):
    pseudo=request.form.get("pseudo")
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    mail = request.form.get("email")
    dDnA =request.form.get("dateDN")
    lDN = request.form.get("lDN")
    adresseA = request.form.get("adresse")
    numSecu = request.form.get("numSec")
    numCNI = request.form.get("numCNI")
    dateDel = request.form.get("dateDelivrance")
    dateExp = request.form.get("dateExpiration")
    mod_artiste(id,pseudo, nom, prenom, mail, dDnA, lDN, adresseA, numSecu, numCNI, dateDel, dateExp)
    return render_template("liste_artiste.html",title="Les Artistes", lArt=get_info_artiste())

@app.route("/modif-artiste-grp/<int:id>", methods =["POST"])
def modif_artiste_grp(id):
    pseudo=request.form.get("pseudo")
    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    mail = request.form.get("email")
    dDnA =request.form.get("dateDN")
    lDN = request.form.get("lDN")
    adresseA = request.form.get("adresse")
    numSecu = request.form.get("numSec")
    numCNI = request.form.get("numCNI")
    dateDel = request.form.get("dateDelivrance")
    dateExp = request.form.get("dateExpiration")
    mod_artiste(id,pseudo, nom, prenom, mail, dDnA, lDN, adresseA, numSecu, numCNI, dateDel, dateExp)
    return render_template("liste_groupes.html",title="Les Groupes",groupes=get_dico_grps())


@app.route("/retour/<string:typeOrga>")
def retour(typeOrga):
    if typeOrga == "Technique":
        return redirect(url_for("accueil_technique"))
    else:
        return redirect(url_for("accueil_bien_etre"))

@app.route("/retourFiche/<int:conc>")
def retourFiche(conc):
    return render_template("Consulter_fiches.html",conc=get_info_un_concert(conc))

