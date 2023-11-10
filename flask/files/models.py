from sqlalchemy import Column, Integer, String, Boolean, Date, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
from .app import db
from flask_login import UserMixin
from .app import login_manager

@login_manager.user_loader
def load_user(nomOrga):
    return Organisation.query.get(nomOrga)

class Musicien(db.Model):
    __tablename__ = 'MUSICIEN'
    musicienID = Column(Integer, primary_key=True,autoincrement=True)
    nomMusicien = Column(String(50))

class MaterielArtiste(db.Model):
    __tablename__ = 'MATERIELARTISTE'
    materielArtisteID = Column(Integer, primary_key=True,autoincrement=True)
    nomMaterielArt = Column(String(200))
    disponible = Column(Boolean)

class RoleP(db.Model):
    __tablename__ = 'ROLEP'
    roleID = Column(Integer, primary_key=True,autoincrement=True)
    nomRole = Column(String(50))

class Organisation(db.Model, UserMixin):
    __tablename__ = 'ORGANISATION'
    nomOrga = db.Column(String(50), primary_key=True)
    motDePasse = db.Column(String(500))
    typeOrga = db.Column(String(50))

    def get_id(self):
        return self.nomOrga

class TypePlace(db.Model):
    __tablename__ = 'TYPEPLACE'
    typePlaceID = Column(Integer, primary_key=True,autoincrement=True)
    nomPlace = Column(String(50))
    descriptionP = Column(Text)

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

class Vehicule(db.Model):
    __tablename__ = 'VEHICULE'
    immatriculation = Column(String(255), primary_key=True,autoincrement=True)
    typeVehicule = Column(String(255))
    capacitéV = Column(Integer)

class Materiel(db.Model):
    __tablename__ = 'MATERIEL'
    materielID = Column(Integer, primary_key=True,autoincrement=True)
    nomMateriel = Column(String(255))

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

class PersonelTechnique(db.Model):
    __tablename__ = 'PERSONELTECHNIQUE'
    personelTechniqueID = Column(Integer, primary_key=True,autoincrement=True)
    roleID = Column(Integer, ForeignKey('ROLEP.roleID'))
    nomP = Column(String(50))
    prenomP = Column(String(50))
    role = relationship(RoleP)

class Plan(db.Model):
    __tablename__ = 'PLAN'
    planID = Column(Integer, primary_key=True,autoincrement=True)
    planScene = Column(Integer)  # Utilisez le type de données approprié pour BLOB
    planFeu = Column(Integer)
    salleID = Column(Integer, ForeignKey('SALLE.salleID'))
    salle = relationship(Salle)

class Hebergement(db.Model):
    __tablename__ = 'HEBERGMENT'
    hebergementID = Column(Integer, primary_key=True, autoincrement=True)
    nomHebergement = Column(String(255), nullable=False)
    capacitéH = Column(Integer, nullable=False)
    qualitéH = Column(Integer, nullable=False)
    lieuID = Column(Integer, ForeignKey('LIEU.lieuID'))
    lieu = relationship(Lieu)

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
        

class MusicienAdditionnel(db.Model):
    __tablename__ = 'MUSICIENADDITIONEL'
    musicienID = Column(Integer, ForeignKey('MUSICIEN.musicienID'), primary_key=True)
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    musicien = relationship(Musicien)
    concert = relationship(Concert)

class Transporte(db.Model):
    __tablename__ = 'TRANSPORTE'
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    immatriculation = Column(String(50), ForeignKey('VEHICULE.immatriculation'), primary_key=True)
    concert = relationship(Concert)
    vehicule = relationship(Vehicule)

class Necessiter(db.Model):
    __tablename__ = 'NECESSITER'
    materielID = Column(Integer, ForeignKey('MATERIEL.materielID'), primary_key=True)
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    materiel = relationship(Materiel)
    concert = relationship(Concert)

class Composer(db.Model):
    __tablename__ = 'COMPOSER'
    artisteID = Column(Integer, ForeignKey('ARTISTE.artisteID'), primary_key=True)
    groupeID = Column(Integer, ForeignKey('GROUPE.groupeID'), primary_key=True)
    artiste = relationship(Artiste)
    groupe = relationship(Groupe)

class Utilise(db.Model):
    __tablename__ = 'UTILISE'
    materielArtisteID = Column(Integer, ForeignKey('MATERIELARTISTE.materielArtisteID'), primary_key=True)
    groupeID = Column(Integer, ForeignKey('GROUPE.groupeID'), primary_key=True)
    quantiteMaterielArt = Column(Integer)
    materielArtiste = relationship(MaterielArtiste)
    groupe = relationship(Groupe)

class Participe(db.Model):
    __tablename__ = 'PARTICIPE'
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    groupeID = Column(Integer, ForeignKey('GROUPE.groupeID'), primary_key=True)
    concert = relationship(Concert)
    groupe = relationship(Groupe)

class Prepare(db.Model):
    __tablename__ = 'PREPARE'
    personelTechniqueID = Column(Integer, ForeignKey('PERSONELTECHNIQUE.personelTechniqueID'), primary_key=True)
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    concert = relationship(Concert)
    personelTechnique = relationship(PersonelTechnique)


class SalleTypePlace(db.Model):
    __tablename__ = 'SALLETYPEPLACE'
    typePlaceID = Column(Integer, ForeignKey('TYPEPLACE.typePlaceID'), primary_key=True)
    salleID = Column(Integer, ForeignKey('SALLE.salleID'), primary_key=True)
    capaciteS = Column(Integer)
    typePlace = relationship(TypePlace)
    salle = relationship(Salle)

class Organiser(db.Model):
    __tablename__ = 'ORGANISER'
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    nomOrga = Column(String(50), ForeignKey('ORGANISATION.nomOrga'), primary_key=True)
    concert = relationship(Concert)
    organisation = relationship(Organisation)