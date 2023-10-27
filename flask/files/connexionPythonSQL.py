from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import func
import pymysql

pymysql.install_as_MySQLdb()
Base = declarative_base()

class Musicien(Base):
    __tablename__ = 'MUSICIEN'
    musicienID = Column(Integer, primary_key=True)
    nomMusicien = Column(String(50))

class MaterielArtiste(Base):
    __tablename__ = 'MATERIELARTISTE'
    materielArtisteID = Column(Integer, primary_key=True)
    nomMaterielArt = Column(String(200))
    disponible = Column(Boolean)

class RoleP(Base):
    __tablename__ = 'ROLEP'
    roleID = Column(Integer, primary_key=True)
    nomRole = Column(String(50))

class Organisation(Base):
    __tablename__ = 'ORGANISATION'
    nomOrga = Column(String(50), primary_key=True)
    motDePasse = Column(String(50))
    typeOrga = Column(String(50))

class TypePlace(Base):
    __tablename__ = 'TYPEPLACE'
    typePlaceID = Column(Integer, primary_key=True)
    nomPlace = Column(String(50))
    descriptionP = Column(Text)

class Lieu(Base):
    __tablename__ = 'LIEU'
    lieuID = Column(Integer, primary_key=True)
    nomVille = Column(String(255))
    adresseL = Column(String(255))
    departement = Column(Integer)

class Artiste(Base):
    __tablename__ = 'ARTISTE'
    artisteID = Column(Integer, primary_key=True)
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

class Vehicule(Base):
    __tablename__ = 'VEHICULE'
    immatriculation = Column(String(255), primary_key=True)
    typeVehicule = Column(String(255))
    capacitéV = Column(Integer)

class Materiel(Base):
    __tablename__ = 'MATERIEL'
    materielID = Column(Integer, primary_key=True)
    nomMateriel = Column(String(255))

class Groupe(Base):
    __tablename__ = 'GROUPE'
    groupeID = Column(Integer, primary_key=True)
    nomGroupe = Column(String(255))

class Salle(Base):
    __tablename__ = 'SALLE'
    salleID = Column(Integer, primary_key=True)
    nomSalle = Column(String(255))
    capaciteTotaleSalle = Column(Integer)
    planSalle = Column(Integer)  # Utilisez le type de données approprié pour BLOB, selon votre base de données
    dimensionOuverture = Column(Float)
    dimensionProfondeur = Column(Float)
    lieuID = Column(Integer, ForeignKey('LIEU.lieuID'))
    lieu = relationship(Lieu)

class PersonelTechnique(Base):
    __tablename__ = 'PERSONELTECHNIQUE'
    personelTechniqueID = Column(Integer, primary_key=True)
    roleID = Column(Integer, ForeignKey('ROLEP.roleID'))
    nomP = Column(String(50))
    prenomP = Column(String(50))
    role = relationship(RoleP)

class Plan(Base):
    __tablename__ = 'PLAN'
    planID = Column(Integer, primary_key=True)
    planScene = Column(Integer)  # Utilisez le type de données approprié pour BLOB
    planFeu = Column(Integer)
    salleID = Column(Integer, ForeignKey('SALLE.salleID'))
    salle = relationship(Salle)

class Hebergement(Base):
    __tablename__ = 'HEBERGMENT'
    hebergementID = Column(Integer, primary_key=True, autoincrement=True)
    nomHebergement = Column(String(255), nullable=False)
    capacitéH = Column(Integer, nullable=False)
    qualitéH = Column(Integer, nullable=False)
    lieuID = Column(Integer, ForeignKey('LIEU.lieuID'))
    lieu = relationship(Lieu)

class MaterielSalle(Base):
    __tablename__ = 'MATERIELSALLE'
    materielSalleID = Column(Integer, primary_key=True)
    salleID = Column(Integer, ForeignKey('SALLE.salleID'))
    nomMaterielS = Column(String(255))
    disponible = Column(Boolean)
    salle = relationship(Salle)

class Concert(Base):
    __tablename__ = 'CONCERT'
    concertID = Column(Integer, primary_key=True)
    nomConcert = Column(String(255))
    dateDebutConcert = Column(Date)
    dateFinConcert = Column(Date)
    ficheTechnique = Column(Text)
    catering = Column(Text)
    salleID = Column(Integer, ForeignKey('SALLE.salleID'))
    groupeID = Column(Integer, ForeignKey('GROUPE.groupeID'))
    salle = relationship(Salle)
    groupe = relationship(Groupe)

class MusicienAdditionnel(Base):
    __tablename__ = 'MUSICIENADDITIONEL'
    musicienID = Column(Integer, ForeignKey('MUSICIEN.musicienID'), primary_key=True)
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    musicien = relationship(Musicien)
    concert = relationship(Concert)

class Transporte(Base):
    __tablename__ = 'TRANSPORTE'
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    immatriculation = Column(String(50), ForeignKey('VEHICULE.immatriculation'), primary_key=True)
    concert = relationship(Concert)
    vehicule = relationship(Vehicule)

class Necessiter(Base):
    __tablename__ = 'NECESSITER'
    materielID = Column(Integer, ForeignKey('MATERIEL.materielID'), primary_key=True)
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    quantiteM = Column(Integer)
    materiel = relationship(Materiel)
    concert = relationship(Concert)

class Composer(Base):
    __tablename__ = 'COMPOSER'
    artisteID = Column(Integer, ForeignKey('ARTISTE.artisteID'), primary_key=True)
    groupeID = Column(Integer, ForeignKey('GROUPE.groupeID'), primary_key=True)
    artiste = relationship(Artiste)
    groupe = relationship(Groupe)

class Utilise(Base):
    __tablename__ = 'UTILISE'
    materielArtisteID = Column(Integer, ForeignKey('MATERIELARTISTE.materielArtisteID'), primary_key=True)
    groupeID = Column(Integer, ForeignKey('GROUPE.groupeID'), primary_key=True)
    quantiteMaterielArt = Column(Integer)
    materielArtiste = relationship(MaterielArtiste)
    groupe = relationship(Groupe)

class Participe(Base):
    __tablename__ = 'PARTICIPE'
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    artisteID = Column(Integer, ForeignKey('ARTISTE.artisteID'), primary_key=True)
    concert = relationship(Concert)
    artiste = relationship(Artiste)

class Prepare(Base):
    __tablename__ = 'PREPARE'
    personelTechniqueID = Column(Integer, ForeignKey('PERSONELTECHNIQUE.personelTechniqueID'), primary_key=True)
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    concert = relationship(Concert)
    personelTechnique = relationship(PersonelTechnique)

class Invitation(Base):
    __tablename__ = 'INVITATION'
    typePlaceID = Column(Integer, ForeignKey('TYPEPLACE.typePlaceID'), primary_key=True)
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    quantiteInv = Column(Integer)
    typePlace = relationship(TypePlace)
    concert = relationship(Concert)

class SalleTypePlace(Base):
    __tablename__ = 'SALLETYPEPLACE'
    typePlaceID = Column(Integer, ForeignKey('TYPEPLACE.typePlaceID'), primary_key=True)
    salleID = Column(Integer, ForeignKey('SALLE.salleID'), primary_key=True)
    capaciteS = Column(Integer)
    typePlace = relationship(TypePlace)
    salle = relationship(Salle)

class Organiser(Base):
    __tablename__ = 'ORGANISER'
    concertID = Column(Integer, ForeignKey('CONCERT.concertID'), primary_key=True)
    nomOrga = Column(String(50), ForeignKey('ORGANISATION.nomOrga'), primary_key=True)
    concert = relationship(Concert)
    organisation = relationship(Organisation)

if __name__ == '__main__':

    login='chabilan'
    passwd='chabilan'
    serveur='servinfo-maria'
    bd='DBchabilan '
    engine=create_engine('mysql+mysqldb://'+login+':'+passwd+'@'+serveur+'/'+bd, echo=False)


    Session = sessionmaker(bind=engine)
    session = Session()
