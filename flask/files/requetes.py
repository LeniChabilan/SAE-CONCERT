from .models import Concert, Groupe, Artiste, Materiel, MaterielSalle, Composer, Participe, Salle, Necessiter, Organiser, Plan
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import pymysql
from datetime import datetime
import os

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import base64

Base = declarative_base()
from .app import db
from flask_login import UserMixin
from .app import login_manager

def login():
    login='chabilan'
    passwd='chabilan'
    serveur='servinfo-maria'
    bd='DBchabilan'
    engine=create_engine('mysql+mysqldb://'+login+':'+passwd+'@'+serveur+'/'+bd, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_concert_filtre(dateDebut, dateFin, salleId, groupeId):
    concFiltre = db.session.query(Concert)

    if salleId is not None:
        concFiltre = concFiltre.filter(Concert.salleID == salleId)

    if groupeId is not None:
        concFiltre = concFiltre.filter(Concert.groupeID == groupeId)

    if dateDebut is not None:
        concFiltre = concFiltre.filter(Concert.dateDebutConcert >= dateDebut)

    if dateFin is not None:
        concFiltre = concFiltre.filter(Concert.dateFinConcert <= dateFin)

    return concFiltre.all()



def get_info_concert():
    return db.session.query(Concert).all()

def get_info_groupe():
    return db.session.query(Groupe).all()

def get_info_un_groupe(id):
    return db.session.query(Groupe).filter(Groupe.groupeID==id).first()

def get_info_artiste():
    return db.session.query(Artiste).all()

def get_info_un_artiste(id):
    return db.session.query(Artiste).filter(Artiste.artisteID==id).first()

def get_info_un_concert(id):
    return db.session.query(Concert).filter(Concert.concertID==id).first()

def get_id_artiste_par_groupe(idG):
    session = login()
    grps=session.query(Composer).filter(Composer.groupeID==idG).all()
    liste_artID=[]
    for grp in grps:
        liste_artID.append(grp.artisteID)
    return liste_artID

def get_liste_artiste(liste_id):
    session = login()
    liste_art=[]
    for idA in liste_id:
        arti=session.query(Artiste).filter(Artiste.artisteID==idA).first()
        liste_art.append(arti)
    return liste_art

def get_dico_grps():
    dicoGr={}
    grps=get_info_groupe()
    for grp in grps:
        idG=grp.groupeID
        liste_idA=get_id_artiste_par_groupe(idG)
        liste_arti=get_liste_artiste(liste_idA)
        dicoGr[grp]=liste_arti
    return dicoGr


def supprimer_groupe(grpID):
    try :
        db.session.query(Participe).filter_by(groupeID=grpID).delete(synchronize_session=False)
        db.session.query(Composer).filter_by(groupeID=grpID).delete(synchronize_session=False)
        db.session.query(Concert).filter_by(groupeID=grpID).delete(synchronize_session=False)
        db.session.query(Groupe).filter_by(groupeID=grpID).delete(synchronize_session=False)
        db.session.commit()
        return "Groupe supprimée avec succès."
    except pymysql.IntegrityError:
        # Si une contrainte de clé étrangère empêche la suppression, gérez l'erreur ici
        db.session.rollback()
        return "Erreur : Impossible de supprimer le groupe en raison de contraintes de clé étrangère."

def supprimer_concert(concID):
    try:
        # Supprimez le concert et toutes les lignes liées dans d'autres tables
        
        db.session.query(Plan).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Necessiter).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Participe).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Organiser).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Concert).filter_by(concertID=concID).delete(synchronize_session=False)

        db.session.commit()
        return "Concert et enregistrements liés supprimés avec succès."
    except pymysql.IntegrityError:
        # Si une contrainte de clé étrangère empêche la suppression, gérez l'erreur ici
        db.session.rollback()
        return "Erreur : Impossible de supprimer le concert et ses enregistrements liés en raison de contraintes de clé étrangère."

def mod_concert(id,nom, dateD, dateF, salle, groupe):
    session = login()
    conc = session.query(Concert).filter(Concert.concertID == id).first()
    if conc:
        conc.nomConcert = nom
        conc.dateDebutConcert = dateD
        conc.dateFinConcert = dateF
        conc.salleID = get_id_salle_by_nom(salle)
        conc.groupeID = get_id_groupe_by_nom(groupe)
        session.commit()
    else:
        print("Le concert n'a pas été trouvé.")


def mod_artiste(id,pseudo, nom, prenom, mail, dDnA, lDN, adresseA, numSecu, numCNI, dateDel, dateExp):
    session = login()
    arti = session.query(Artiste).filter(Artiste.artisteID == id).first()
    if arti:
        arti.pseudoArtiste=pseudo
        arti.nomA=nom
        arti.prenomA=prenom
        arti.mailA=mail
        arti.DdNA=dDnA
        arti.LdN=lDN
        arti.adresseA=adresseA
        arti.numSecuriteSociale=numSecu
        arti.numCNI=numCNI
        arti.dateDelivranceCNI=dateDel
        arti.dateExpirationCNI=dateExp
        session.commit()
    else:
        print("L'artiste n'a pas été trouvé.")

def get_max_id():
    session = login()
    if session.query(func.max(Concert.concertID)).all()[0][0] is None:
        return 1
    return session.query(func.max(Concert.concertID)).all()[0][0] + 1

def get_max_id_groupe():
    session = login()
    if session.query(func.max(Groupe.groupeID)).all()[0][0] is None:
        return 1
    return session.query(func.max(Groupe.groupeID)).all()[0][0] + 1

def get_id_salle_by_nom(nom):
    session = login()
    return session.query(Salle.salleID).filter_by(nomSalle = nom).limit(1).all()[0][0]

def get_id_groupe_by_nom(nom):
    session = login()
    return session.query(Groupe.groupeID).filter_by(nomGroupe = nom).limit(1).all()[0][0]

def ajouter_concert(Nom, dateDebut, dateFin, ficheTechnique, catering, salle, groupe,lien):
    session = login()
    concert = Concert(Nom, datetime.strptime(dateDebut,"%Y-%m-%d").date(), datetime.strptime(dateFin,"%Y-%m-%d").date(), ficheTechnique, catering, get_id_salle_by_nom(salle), get_id_groupe_by_nom(groupe),lien)
    session.add(concert)
    session.commit()

def chercher_groupe(nom):
    session = login()
    groupe = session.query(Groupe).filter_by(nomGroupe=nom).all()
    if groupe != []:    
        session.expunge_all()
        session.close()    
        return groupe[0]
    else:
        grp = Groupe(nom)
        session.add(grp)
        session.commit()
        session.refresh(grp)
        session.close()
        return grp

def get_liste_salle():
    session = login()
    return session.query(Salle).all()

def get_liste_groupe():
    session = login()
    return session.query(Groupe).all()

def get_artiste_id_groupe(id):
    session = login()
    artistes = session.query(Composer.artisteID).filter_by(groupeID=id).all()
    session.expunge_all()
    session.close() 
    return artistes

def get_concert_id_nouv():
    session=login()
    res=session.query(func.max(Concert.concertID)).all()[0][0]+1
    session.close()
    return res




def supprimer_artiste(artID):
    try:
        # Supprimez le concert et toutes les lignes liées dans d'autres tables
        db.session.query(Composer).filter_by(artisteID=artID).delete(synchronize_session=False)
        db.session.query(Artiste).filter_by(artisteID=artID).delete(synchronize_session=False)

        db.session.commit()
        return "Artiste et enregistrements liés supprimés avec succès."
    except pymysql.IntegrityError:
        # Si une contrainte de clé étrangère empêche la suppression, gérez l'erreur ici
        db.session.rollback()
        return "Erreur : Impossible de supprimer l'artiste et ses enregistrements liés en raison de contraintes de clé étrangère."
    
def get_plan_concert(idconcert):
    session = login()
    res= session.query(Plan).filter_by(concertID=idconcert).all()
    return res
    # res1=[]
    # for val in res:
    #     res1.append(val[0])
    # return res1

def sup_plan_id(id):
    session = login()
    try:
        session.query(Plan).filter_by(planID=id).delete(synchronize_session=False)
        session.commit()
        return "suppression effectuée"
    except pymysql.IntegrityError:
        # Si une contrainte de clé étrangère empêche la suppression, gérez l'erreur ici
        db.session.rollback()
        return "Erreur : Impossible de supprimer le plan et ses enregistrements liés en raison de contraintes de clé étrangère."


def ajouter_artiste(pseudo, nom, prenom, email, DdN, lieuNaissance, adresse, numSecu, numCNI, debutCNI, finCNI, idGroupe):
    session = login()
    artiste = Artiste(pseudo, nom, prenom, email, DdN, lieuNaissance, adresse, numSecu, numCNI, debutCNI, finCNI, 1)
    session.add(artiste)
    session.commit()
    composer = Composer(session.query(Artiste.artisteID).filter_by(nomA = nom).limit(1).all()[0][0], idGroupe)
    session.add(artiste)
    session.add(composer)
    session.commit()
    session.close() 


def get_max_id_Materiel():
    session = login()
    if session.query(func.max(Materiel.materielID)).all()[0][0] is None:
        return 1
    return session.query(func.max(Materiel.materielID)).all()[0][0] + 1
    
def ajout_nessecite_concert(objet, concert, description, quantite):
    session = login()
    
    # Recherche de l'id du matériel
    materiel_id_query = session.query(Materiel.materielID).filter_by(nomMateriel=objet).first()
    
    if materiel_id_query:
        id = materiel_id_query[0]
    else:
        # Si la recherche ne renvoie rien, créez un nouvel ID
        id = get_max_id_Materiel()
        materiel = Materiel(id, objet)
        session.add(materiel)
    
    # Vérifiez si la relation Necessiter existe déjà
    necessiter_query = session.query(Necessiter).filter_by(materielID=id, concertID=concert).first()
    
    if necessiter_query is None:
        # Si la relation n'existe pas, ajoutez-la
        necessite = Necessiter(id, concert, description, quantite)
        session.add(necessite)

    session.commit()
    session.close()

def get_liste_neccessite(concert):
    session = login()
    # res = []
    necessaire = session.query(Necessiter).filter_by(concertID=concert).all()
    # for row in necessaire:
    #     liste = []
    #     description = row.description
    #     nom_objet = session.query(Materiel.nomMateriel).filter_by(materielID = row.materielID).first()[0]
    #     liste.append(nom_objet)
    #     liste.append(description)
    #     liste.append(row.quantite)
    #     res.append(liste)
    # session.expunge_all()
    # session.close()
    return necessaire
    
def get_info_materiel_salle(concert):
    session = login()
    nom_salle = session.query(Concert.salleID).filter(Concert.concertID==concert).first()[0]
    a= session.query(MaterielSalle).filter(MaterielSalle.salleID==nom_salle).all()
    session.expunge_all()
    session.close()
    return a

def supp_necessite(nom_necessite):
    id = db.session.query(Materiel.materielID).filter_by(nomMateriel = nom_necessite).first()[0]
    print(id)
    try:
        db.session.query(Necessiter).filter(Necessiter.materielID == id).delete(synchronize_session=False)
        db.session.commit()
        print("Removing")
        db.session.close()
    except pymysql.IntegrityError:
        # Si une contrainte de clé étrangère empêche la suppression, gérez l'erreur ici
        db.session.rollback()
        print("not Removing")

def ajouter_plan(concertID):
    session = login()
    files = os.listdir("./static/temp/plan/")
    for file in files:
        file_path = "./static/temp/plan/" + file
        with open(file_path, 'rb') as pdf_file:
            pdf_data = base64.b64encode(pdf_file.read())
        plan = Plan(pdf_data, concertID)
        session.add(plan)
        session.commit()
        os.remove(file_path)
    session.close()
    
def ajouter_mat(idC,nom,quantite,description):
    session = login()
    idM=get_max_id_Materiel()
    mat=Materiel(idM,nom)
    session.add(mat)
    session.commit()
    ajout_nessecite_concert(nom,idC,description,quantite)
    session.close()
     

    
def ajouter_rider(concertID):
    session = login()
    files = os.listdir("./static/temp/rider/")
    for file in files:
        file_path = "./static/temp/rider/" + file
        with open(file_path, 'rb') as pdf_file:
            pdf_data = base64.b64encode(pdf_file.read())
        concert = session.query(Concert).filter(Concert.concertID == concertID).first()
        concert.ficheRider = pdf_data
        session.commit()
        os.remove(file_path)
    session.close()

def generate_pdf(text):
    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=letter)
    pdf_canvas.drawString(100, 750, text)
    pdf_canvas.save()
    buffer.seek(0)
    return buffer

def pdf_base_64(text):
    pdf_buffer = generate_pdf(text)

    # Convertir le contenu du PDF en base64
    pdf_content_base64 = base64.b64encode(pdf_buffer.getvalue())
    # print(pdf_content_base64)  
    # print(pdf_content_base64.encode('utf-8'))
    # Afficher le contenu base64
    return pdf_content_base64

def get_concert_by_name(nomConcert):
    session = login()
    concert = session.query(Concert.concertID).filter_by(nomConcert=nomConcert).limit(1).all()[0][0]
    return concert

def modif_fiche_technique(concertID, ficheT):
    session = login()
    concert = session.query(Concert).filter(Concert.concertID == concertID).first()
    concert.ficheTechnique = ficheT
    session.commit()
    session.close()

def modif_fiche_acc(concertID, ficheA):
    session = login()
    concert = session.query(Concert).filter(Concert.concertID == concertID).first()
    concert.catering = ficheA
    session.commit()
    session.close()

def get_artiste_groupe(id):
    session = login()
    artistesID = session.query(Composer.artisteID).filter_by(groupeID=id).all()
    lesArtistes = []
    for artiste in artistesID:
        lesArtistes.append(session.query(Artiste).filter(Artiste.artisteID == artiste[0]).first())
    session.expunge_all()
    session.close() 
    return lesArtistes

def get_groupe_id(id):
    session = login()
    groupe_id=session.query(Groupe).filter(Groupe.groupeID==id).all()
    session.close() 
    return groupe_id

def get_dico_grps_art(id):
    dicoGr={}
    grps=get_groupe_id(id)
    for grp in grps:
        idG=grp.groupeID
        liste_idA=get_id_artiste_par_groupe(idG)
        liste_arti=get_liste_artiste(liste_idA)
        dicoGr[grp]=liste_arti
    return dicoGr

def get_nom_groupe(id):
    session = login()
    nom=session.query(Groupe.nomGroupe).filter(Groupe.groupeID==id).all()
    session.close() 
    return nom[0][0]
