from .models import Concert, Groupe, Artiste, Composer, Participe, Salle, MusicienAdditionnel, Transporte, Necessiter, Prepare, Organiser , Utilise
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import pymysql
from datetime import datetime

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
        db.session.query(Utilise).filter_by(groupeID=grpID).delete(synchronize_session=False)
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
        db.session.query(MusicienAdditionnel).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Transporte).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Necessiter).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Participe).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Prepare).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Organiser).filter_by(concertID=concID).delete(synchronize_session=False)
        db.session.query(Concert).filter_by(concertID=concID).delete(synchronize_session=False)

        db.session.commit()
        return "Concert et enregistrements liés supprimés avec succès."
    except pymysql.IntegrityError:
        # Si une contrainte de clé étrangère empêche la suppression, gérez l'erreur ici
        db.session.rollback()
        return "Erreur : Impossible de supprimer le concert et ses enregistrements liés en raison de contraintes de clé étrangère."

def mod_concert(id,nom, dateD, dateF, ficheTech, catering, salle, groupe):
    session = login()
    conc = session.query(Concert).filter(Concert.concertID == id).first()
    if conc:
        conc.nomConcert = nom
        conc.dateDebutConcert = dateD
        conc.dateFinConcert = dateF
        conc.ficheTechnique = ficheTech
        conc.catering = catering
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

def ajouter_concert(Nom, dateDebut, dateFin, ficheTechnique, catering, salle, groupe):
    session = login()
    concert = Concert(Nom, datetime.strptime(dateDebut,"%Y-%m-%d").date(), datetime.strptime(dateFin,"%Y-%m-%d").date(), ficheTechnique, catering, get_id_salle_by_nom(salle), get_id_groupe_by_nom(groupe))
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

def get_artiste_groupe(id):
    session = login()
    artistes = session.query(Composer.artisteID).filter_by(groupeID=id).all()
    session.expunge_all()
    session.close() 
    return artistes

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
    
def ajouter_artiste(pseudo, nom, prenom, email, DdN, lieuNaissance, adresse, numSecu, numCNI, debutCNI, finCNI, idGroupe):
    session = login()
    artiste = Artiste(pseudo, nom, prenom, email, DdN, lieuNaissance, adresse, numSecu, numCNI, debutCNI, finCNI, 1)
    session.add(artiste)
    session.commit()
    print(session.query(Artiste.artisteID).filter_by(nomA = nom).limit(1).all()[0][0])
    composer = Composer(session.query(Artiste.artisteID).filter_by(nomA = nom).limit(1).all()[0][0], idGroupe)
    session.add(artiste)
    session.add(composer)
    session.commit()
    session.close() 
