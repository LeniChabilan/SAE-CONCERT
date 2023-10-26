
create Table MUSICIEN(
    musicienID int PRIMARY KEY,
    nomMusicien VARCHAR(50)
);

create Table MATERIELARTISTE(
    materielArtisteID int PRIMARY KEY,
    nomMaterielArt VARCHAR(200),
    disponible boolean 
);

create Table ROLEP(
    roleID int PRIMARY KEY,
    nomRole VARCHAR(50)
);

create Table ORGANISATION(
    nomOrga varchar(50) PRIMARY KEY,
    motDePasse varchar(50),
    typeOrga VARCHAR(50)
);

create Table TYPEPLACE(
    typePlaceID int PRIMARY KEY,
    nomPlace varchar(50),
    descriptionP TEXT
);

-- Table pour stocker les informations sur les lieux des concerts et des activités annexes
CREATE TABLE LIEU (
    lieuID INT PRIMARY KEY,
    nomVille VARCHAR(255),
    adresseL VARCHAR(255),
    departement INT(3)
);


-- Table pour stocker les informations sur les Artistes
CREATE TABLE ARTISTE(
    artisteID INT PRIMARY KEY,
    pseudoArtiste VARCHAR(255),
    nomA VARCHAR(255),
    prenomA VARCHAR(255),
    mailA VARCHAR(255),
    DdNA DATE,
    LdN VARCHAR(255),
    adresseA VARCHAR(255),
    numSecuriteSociale INT,
    numCNI INT,
    dateDelivranceCNI DATE,
    dateExpirationCNI DATE,
    dansGroupe BOOLEAN 

);

CREATE TABLE VEHICULE(
    immatriculation VARCHAR(255) PRIMARY KEY,
    typeVehicule VARCHAR(255),
    capacitéV INT
);

CREATE TABLE MATERIEL(
    materielID int PRIMARY KEY,
    nomMateriel VARCHAR(255)
);


CREATE TABLE GROUPE(
    groupeID int PRIMARY KEY,
    nomGroupe varchar(255)
);

CREATE TABLE SALLE (
    salleID INT PRIMARY KEY,
    nomSalle VARCHAR(255),
    capaciteTotaleSalle INT,
    planSalle BLOB,
    dimensionOuverture float,
    dimensionProfondeur float,
    lieuID INT,
    FOREIGN KEY (lieuID) REFERENCES LIEU(lieuID)
);

CREATE TABLE PERSONELTECHNIQUE(
    personelTechniqueID int PRIMARY KEY,
    roleID int ,
    nomP varchar(50),
    prenomP VARCHAR(50),
    FOREIGN KEY (roleID) REFERENCES ROLEP(roleID)
);

CREATE TABLE PLAN(
    planID int PRIMARY KEY,
    planScene BLOB,
    planFeu int,
    salleID int,
    FOREIGN KEY (salleID) REFERENCES SALLE(salleID)
);

-- Table pour stocker les informations sur l'hebergement
CREATE TABLE HEBERGMENT (
    hebergementID INT PRIMARY KEY AUTO_INCREMENT,
    nomHebergement VARCHAR(255) NOT NULL,
    capacitéH INT NOT NULL,
    qualitéH INT NOT NULL,
    lieuID int,
    prix int,
    FOREIGN KEY (lieuID) REFERENCES LIEU(lieuID)
);

create Table MATERIELSALLE(
    materielSalleID int PRIMARY KEY,
    salleID INT,
    nomMaterielS VARCHAR(255),
    disponible BOOLEAN,
    FOREIGN KEY (salleID) REFERENCES SALLE(salleID)
);

-- Table pour stocker les informations sur les concerts
CREATE TABLE CONCERT (
    concertID INT PRIMARY KEY,
    nomConcert varchar(255),
    dateDebutConcert DATE,
    dateFinConcert DATE,
    ficheTechnique TEXT,
    catering TEXT,
    salleID int,
    groupeID int,
    FOREIGN KEY (salleID) REFERENCES SALLE(salleID),
    FOREIGN KEY (groupeID) REFERENCES GROUPE(groupeID)
); 


CREATE TABLE MUSICIENADDITIONEL(
    musicienID int,
    concertID int,
    FOREIGN KEY (musicienID) REFERENCES MUSICIEN(musicienID),
    FOREIGN KEY (concertID) REFERENCES CONCERT(concertID)
);

CREATE TABLE TRANSPORTE(
    concertID INT,
    immatriculation varchar(50),
    FOREIGN KEY (concertID) REFERENCES CONCERT(concertID),
    FOREIGN KEY (immatriculation) REFERENCES VEHICULE(immatriculation)
);

create Table NECESSITER(
    materielID int,
    concertID int,
    quantiteM int,
    FOREIGN KEY (materielID) REFERENCES MATERIEL(materielID),
    FOREIGN KEY (concertID) REFERENCES CONCERT(concertID)
);


CREATE TABLE COMPOSER(
    artisteID INT,
    groupeID INT,
    FOREIGN KEY (artisteID) REFERENCES ARTISTE(artisteID),
    FOREIGN KEY (groupeID) REFERENCES GROUPE(groupeID)
);


CREATE TABLE UTILISE(
    materielArtisteID int,
    groupeID int,
    quantiteMaterielArt int,
    FOREIGN KEY (materielArtisteID) REFERENCES MATERIELARTISTE(materielArtisteID),
    FOREIGN KEY (groupeID) REFERENCES GROUPE(groupeID)
);

CREATE TABLE PARTICIPE(
    concertId int,
    artisteId int,
    FOREIGN KEY (concertId) REFERENCES CONCERT(concertId),
    FOREIGN KEY (artisteId) REFERENCES ARTISTE(artisteId)
);


CREATE TABLE PREPARE(
    personelTechniqueID int,
    concertID int,
    FOREIGN KEY (concertID) REFERENCES CONCERT(concertId),
    FOREIGN KEY (personelTechniqueID) REFERENCES PERSONELTECHNIQUE(personelTechniqueID)    
);


CREATE TABLE INVITATION(
    typePlaceID int ,
    concertID int ,
    quantiteInv int,
    FOREIGN KEY (concertID) REFERENCES CONCERT(concertId),
    FOREIGN KEY (typePlaceID) REFERENCES TYPEPLACE(typePlaceID)
);

CREATE TABLE SALLETYPEPLACE(
    typePlaceID INT ,
    salleID INT ,
    capaciteS INT,
    FOREIGN KEY (typePlaceID) REFERENCES TYPEPLACE(typePlaceID),
    FOREIGN KEY (salleID) REFERENCES SALLE(salleID)
);

create TABLE ORGANISER(
    concertID int ,
    nomOrga varchar(50) ,
    FOREIGN KEY (nomOrga) REFERENCES ORGANISATION(nomOrga),
    FOREIGN KEY (concertID) REFERENCES CONCERT(concertID)
);




