from sqlalchemy import Column, Integer, String, Boolean, Date, Float, Text, ForeignKey , LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
from .app import db
from flask_login import UserMixin
from .app import login_manager

@login_manager.user_loader
def load_user(nomOrga):
    return Organisation.query.get(nomOrga)


class Organisation(db.Model, UserMixin):
    __tablename__ = 'ORGANISATION'
    nomOrga = db.Column(String(50), primary_key=True)
    motDePasse = db.Column(String(500))
    typeOrga = db.Column(String(50))

    def get_id(self):
        return self.nomOrga



class Lieu(db.Model):
    __tablename__ = 'LIEU'
    lieuID = Column(Integer, primary_key=True,autoincrement=True)
    nomVille = Column(String(255))
    adresseL = Column(String(255))
    departement = Column(Integer)

class Artiste(db.Model):
    __tablename__ = 'ARTISTE'
    artisteID = Column(Integer, primary_key=True,autoincrement=True)
    pseudoArtiste = Column(String(255))
    nomA = Column(String(255))
    prenomA = Column(String(255))
    mailA = Column(String(255))
    DdNA = Column(Date)
    LdN = Column(String(255))
    adresseA = Column(String(255))
    numSecuriteSociale = Column(Integer)
    numCNI = Column(Integer)
    dateDelivranceCNI = Column(Date)
    dateExpirationCNI = Column(Date)
    dansGroupe = Column(Boolean)

    def __init__(self, pseudo, nom, prenom, email, DdN, lieuNaissance, adresse, numSecu, numCNI, debutCNI, finCNI, dansGRoupe):
        self.pseudoArtiste = pseudo
        self.nomA = nom
        self.prenomA = prenom
        self.emailA = email
        self.DdNA = DdN 
        self.LdN = lieuNaissance
        self.adresseA = adresse
        self.numSecuriteSociale = numSecu
        self.numCNI = numCNI
        self.dateDelivranceCNI = debutCNI
        self.dateExpirationCNI = finCNI
        self.dansGroupe = dansGRoupe


class Materiel(db.Model):
    __tablename__ = 'MATERIEL'
    materielID = Column(Integer, primary_key=True,autoincrement=True)
    nomMateriel = Column(String(255))
    
    def __init__(self,materielID,nomMateriel):
        self.materielID = materielID
        self.nomMateriel = nomMateriel

class Groupe(db.Model):
    __tablename__ = 'GROUPE'
    groupeID = Column(Integer, primary_key=True,autoincrement=True)
    nomGroupe = Column(String(255))

    def __init__(self, nomGroupe):
        self.nomGroupe = nomGroupe
        

class Salle(db.Model):
    __tablename__ = 'SALLE'
    salleID = Column(Integer, primary_key=True,autoincrement=True)
    nomSalle = Column(String(255))
    capaciteTotaleSalle = Column(Integer)
    planSalle = Column(Integer)  # Utilisez le type de données approprié pour BLOB, selon votre db.Model de données
    dimensionOuverture = Column(Float)
    dimensionProfondeur = Column(Float)
    lieuID = Column(Integer, ForeignKey('LIEU.lieuID'))
    lieu = relationship(Lieu)


    def __init__(self, planScene, salleId):
        self.planScene = planScene
        self.salleId = salleId

class MaterielSalle(db.Model):
    __tablename__ = 'MATERIELSALLE'
    materielSalleID = Column(Integer, primary_key=True,autoincrement=True)
    salleID = Column(Integer, ForeignKey('SALLE.salleID'))
    nomMaterielS = Column(String(255))
    disponible = Column(Boolean)
    salle = relationship(Salle)

class Concert(db.Model):
    __tablename__ = 'CONCERT'
    concertID = Column(Integer, primary_key=True,autoincrement=True)
    nomConcert = Column(String(255))
    dateDebutConcert = Column(Date)
    dateFinConcert = Column(Date)
    ficheTechnique = Column(Text)
    catering = Column(Text)
    ficheRider = Column(LargeBinary(length=2**32-1))
    salleID = Column(Integer, ForeignKey('SALLE.salleID'))
    groupeID = Column(Integer, ForeignKey('GROUPE.groupeID'))
    salle = relationship(Salle)
    groupe = relationship(Groupe)

    def __init__(self, nom, dateDebut, dateFin, ficheTechnique, catering, salle, groupe):
        self.nomConcert = nom
        self.dateDebutConcert = dateDebut
        self.dateFinConcert = dateFin
        self.ficheTechnique = ficheTechnique
        self.catering = catering
        self.salleID = salle
        self.groupeID = groupe


class Plan(db.Model):
    __tablename__ = 'PLAN'
    planID = Column(Integer, primary_key=True,autoincrement=True)
    planScene = Column(LargeBinary(length=2**32-1))  # Utilisez le type de données approprié pour BLOB
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'))
    concert = relationship(Concert)



class Necessiter(db.Model):
    __tablename__ = 'NECESSITER'
    materielID = Column(Integer, ForeignKey('MATERIEL.materielID'), primary_key=True)
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    description = Column(String(255))
    quantite = Column(Integer)
    materiel = relationship(Materiel)
    concert = relationship(Concert)
    
    def __init__(self,materielID,concertID,description,quantite):
        self.materielID = materielID
        self.concertID = concertID
        self.description = description
        self.quantite = quantite

class Composer(db.Model):
    __tablename__ = 'COMPOSER'
    artisteID = Column(Integer, ForeignKey('ARTISTE.artisteID'), primary_key=True)
    groupeID = Column(Integer, ForeignKey('GROUPE.groupeID'), primary_key=True)
    artiste = relationship(Artiste)
    groupe = relationship(Groupe)

    def __init__(self, artisteID, groupeID):
        self.artisteID = artisteID
        self.groupeID = groupeID



class Participe(db.Model):
    __tablename__ = 'PARTICIPE'
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    groupeID = Column(Integer, ForeignKey('GROUPE.groupeID'), primary_key=True)
    concert = relationship(Concert)
    groupe = relationship(Groupe)



class Organiser(db.Model):
    __tablename__ = 'ORGANISER'
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    nomOrga = Column(String(50), ForeignKey('ORGANISATION.nomOrga'), primary_key=True)
    concert = relationship(Concert)
    organisation = relationship(Organisation)

