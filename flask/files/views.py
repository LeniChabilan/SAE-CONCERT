from .app import app, db
from flask import render_template, url_for, redirect
from flask_login import login_user , current_user, logout_user, login_required
from hashlib import sha256
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField, PasswordField
import base64
# import requests
from werkzeug.utils import secure_filename
import os


from .models import Organisation, Concert
import time
from .requetes import ajouter_concert,  supprimer_concert,supprimer_groupe, get_info_concert, chercher_groupe, mod_concert,  get_info_un_concert, get_liste_salle, get_liste_groupe, get_artiste_groupe, get_info_artiste, get_dico_grps, mod_artiste, mod_artiste, get_info_un_artiste, supprimer_artiste,get_plan_concert, ajouter_artiste,get_concert_filtre,get_id_salle_by_nom,get_id_groupe_by_nom , pdf_base_64, ajouter_plan, get_concert_by_name, modif_fiche_accueil, modif_fiche_technique
from datetime import datetime
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

@app.route("/editer_liste_a_louer", methods = ("GET","POST",))
def editer_liste_a_louer():
    return render_template("editer_liste_a_louer.html")



@app.route("/creation_concert")
def creation_concert():
    return render_template("creation_concert.html", liste_salle=get_liste_salle(), liste_groupe=get_liste_groupe())


@app.route("/liste_concerts/", methods = ("GET","POST",))
def liste_concerts():
    return render_template("liste_concerts.html",title="Les Concerts",concerts=get_info_concert(),liste_salle=get_liste_salle(), liste_groupe=get_liste_groupe())

@app.route("/save-concert/", methods =["POST"])
def save_concert():
    nom = request.form.get("nom")
    dateD = request.form.get("dateD")
    dateF = request.form.get("dateF")
    ficheTech = ""
    catering = ""
    salle = request.form.get("salle")
    groupe = request.form.get("groupe")
    ajouter_concert(nom, dateD, dateF, ficheTech, catering, salle, groupe)
    print(get_concert_by_name(nom))
    return render_template("completer_fiche.html", concertID=get_concert_by_name(nom))


def get_date(concert):
    return concert.dateDebutConcert

def get_nom(concert):
    return concert.nomConcert

def get_salle(concert):
    return concert.salle.nomSalle

def get_groupe(concert):
    return concert.groupe.nomGroupe

@app.route("/filtreConcert", methods=["GET", "POST"])
def filtre_concert():
    if request.method == 'POST':
        # Récupérer les valeurs du formulaire
        date_debut = request.form.get('dateD')
        date_fin = request.form.get('dateF')
        salle = request.form.get('salle')
        groupe = request.form.get('groupe')
        nom=request.form.get('nom')
        filtre=request.form.get('filtre')

        # Appliquer les filtres
        concerts_filtres = []
        concerts = get_info_concert()
        for concert in concerts:
            # Filtre par date
            if nom and nom not in concert.nomConcert:
                continue
            if date_debut:
                dateD=datetime.strptime(date_debut,"%Y-%m-%d").date()
                if concert.dateDebutConcert <= dateD:
                    continue
                
            
            if date_fin:
                dateF=datetime.strptime(date_fin,"%Y-%m-%d").date()
                if concert.dateDebutConcert >= dateF:
                    continue

            # Filtre par salle
            if salle and concert.salle.nomSalle != salle:
                continue

            # Filtre par groupe
            if groupe and concert.groupe.nomGroupe != groupe:
                continue

            # Ajouter le concert filtré à la liste
            concerts_filtres.append(concert)

        if filtre !="aucun":
            if filtre=="dateAsc":
                concerts_filtres.sort(key=get_date)
            elif filtre=="dateDesc":
                concerts_filtres.sort(key=get_date, reverse=True)
            elif filtre=="nom":
                concerts_filtres.sort(key=get_nom)
            elif filtre=="salle":
                concerts_filtres.sort(key=get_salle)
            elif filtre=="groupe":
                concerts_filtres.sort(key=get_groupe)
        # Passer la liste filtrée au modèle
        return render_template("liste_concerts.html", title="Les Concerts", concerts=concerts_filtres, liste_salle=get_liste_salle(), liste_groupe=get_liste_groupe())

    # Si la méthode n'est pas POST, afficher tous les concerts non filtrés
    return render_template("liste_concerts.html", title="Les Concerts", concerts=get_info_concert(), liste_salle=get_liste_salle(), liste_groupe=get_liste_groupe())


@app.route("/sup-concert/<int:id>")
def sup_concert(id):
    supprimer_concert(id)
    return render_template("liste_concerts.html",title="Les Concerts", concerts=get_info_concert(),liste_salle=get_liste_salle(), liste_groupe=get_liste_groupe())

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
    salle = request.form.get("salle")
    groupe = request.form.get("groupe")
    mod_concert(id,nom, dateD, dateF, salle, groupe)
    conc=get_info_concert()
    return render_template("liste_concerts.html", title="Les Concerts",concerts=get_info_concert(),liste_salle=get_liste_salle(), liste_groupe=get_liste_groupe())

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

@app.route("/completer-fiche/<int:concertID>", methods=['GET', 'POST'])
def completer_fiche(concertID):
    return render_template("completer_fiche.html", concertID = concertID)

@app.route("/completer-fiche-pdf/<int:concertID>", methods=['GET', 'POST'])
def completer_fiche_pdf(concertID):
    ficheAccueil = request.form.get("ficheA")
    modif_fiche_accueil(concertID, ficheAccueil)
    ficheTechnique = request.form.get("ficheT")
    modif_fiche_technique(concertID, ficheTechnique)
    return render_template("completer_fiche_pdf.html", concertID = concertID)

@app.route("/fin-inscription/", methods=['GET', 'POST'])
def fin_inscription():
    files = os.listdir("./static/temp/")
    for file in files:
        file_path = "./static/temp/" + file
        with open(file_path, 'rb') as pdf_file:
            pdf_data = base64.b64encode(pdf_file.read())
        ajouter_plan(pdf_data, 1)
    return render_template("fin_inscription.html")

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
        return redirect(url_for("choix_fiche",concert=concert))
    

@app.route("/Consulter_fiches")
def Consulter_fiches():
    return render_template("Consulter_fiches.html")

@app.route("/choix-artiste-groupe/", methods = ("GET","POST",))
def choix_groupes_artistes():
    return render_template("choix_groupes_artistes.html")

@app.route("/visualiser_fiches/<int:conc>", methods = ("GET","POST",))
def visualiser_fiches(conc):
    conc=get_info_un_concert(conc)
    text=conc.ficheTechnique
    pdf=pdf_base_64(text)
    return render_template("visualisation_fiches.html",conc=conc,pdf=pdf)

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

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not os.path.exists(f'{app.config["UPLOADED_TEMP_DEST"]}'):
        os.makedirs(f'{app.config["UPLOADED_TEMP_DEST"]}')
    if request.method == 'POST':
        for key, uploaded_file in request.files.items():
            if key.startswith('file'):
                filename = secure_filename(uploaded_file.filename)
                uploaded_file.save(os.path.join(f'{app.config["UPLOADED_TEMP_DEST"]}/', filename))
    else:
        for stored_file in os.listdir(f'{app.config["UPLOADED_TEMP_DEST"]}/'):
            os.remove(f'{app.config["UPLOADED_TEMP_DEST"]}/{stored_file}')
    return render_template('fin_inscription.html')

@app.route("/retour/<string:typeOrga>")
def retour(typeOrga):
    if typeOrga == "Technique":
        return redirect(url_for("accueil_technique"))
    else:
        return redirect(url_for("accueil_bien_etre"))

@app.route("/retourFiche/<int:conc>")
def retourFiche(conc):
    return render_template("Consulter_fiches.html",conc=get_info_un_concert(conc))


@app.route("/choix-fiche/<int:concert>", methods = ("GET","POST",))
def choix_fiche(concert):
    conc=get_info_un_concert(concert)
    text=conc.catering
    print(text)
    pdf=pdf_base_64(text)
    print(pdf)
    return render_template("choix_fiche.html",pdf=pdf,conc=conc)

