





create Table MUSICIEN(
    musicienID int PRIMARY KEY,
    nomMusicien VARCHAR(50)
);

create Table MUSICIENADDITIONEL(
    musicienID int PRIMARY KEY,
    groupeId int PRIMARY KEY,
    ramene boolean,
    FOREIGN KEY (musicienID) REFERENCES MUSICIEN(musicienID),
    FOREIGN KEY (groupeId) REFERENCES GROUPE(groupeId)
);

---A revoir
create Table GROUPE(
    groupeID int PRIMARY KEY
    
);
create Table APPARTIENT(
    groupeID int PRIMARY KEY,
    artisteId int PRIMARY KEY,
    FOREIGN KEY (groupeID) REFERENCES GROUPE(groupeID),
    FOREIGN KEY (artisteId) REFERENCES ARTISTE(artisteId)
);

create Table UTILISE(
    materielArtisteID int PRIMARY KEY,
    artisteId int PRIMARY KEY,
    quantite int
    FOREIGN KEY (materielArtisteID) REFERENCES MATERIELARTISTE(materielArtisteID),
    FOREIGN KEY (artisteId) REFERENCES ARTISTE(artisteId)
);
create Table MATERIELARTISTE(
    materielArtisteID int PRIMARY KEY,
    nomMateriel VARCHAR(200),
    disponible boolean 
)
create Table PARTICIPE(
    concertId int PRIMARY KEY,
    artisteId int PRIMARY KEY,
    FOREIGN KEY (concertId) REFERENCES CONCERT(concertId),
    FOREIGN KEY (artisteId) REFERENCES ARTISTE(artisteId)
);

create Table ROLE(
    roleID int PRIMARY KEY,
    nomRole VARCHAR(50),
);
create Table ORGANISATION(
    nomOrga varchar(50) PRIMARY KEY,
    motDePasse varchar(50),
    typeOrga VARCHAR(50)
);
create Table PERSONELTECHNIQUE(
    personelTechniqueID int PRIMARY KEY,
    nom varchar(50),
    prenom VARCHAR(50)
);
create Table PREPARE(
    personelTechniqueID int PRIMARY KEY,
    concertID int,
    FOREIGN KEY (concertID) REFERENCES Concert(concertId),
    FOREIGN KEY (personelTechniqueID) REFERENCES PERSONELTECHNIQUE(personelTechniqueID)    
);

create Table TYPEPLACE(
    typeId int PRIMARY KEY,
    nomPlace varchar(50),
    descriptionP TEXT
);
create Table INVITATION(
    typeId int PRIMARY KEY,
    concertID int,
    quantite int
    FOREIGN KEY (concertID) REFERENCES Concert(concertId),
    FOREIGN KEY (typeId) REFERENCES TYPEPLACE(typeId)
);
create Table PLAN(
    planId int PRIMARY KEY,
    planScene BLOB,
    planFeu int
    salleID int,
    FOREIGN KEY (salleID) REFERENCES SALLE(salleID)
);

-- Table pour stocker les informations sur les lieux des concerts et des activités annexes
CREATE TABLE LIEU (
    lieuID INT PRIMARY KEY,
    nomVille VARCHAR(255),
    adresseL VARCHAR(255),
    departement INT(3)
);

CREATE TABLE SALLE (
    salleID INT PRIMARY KEY,
    nomSalle VARCHAR(255),
    capaciteTotaleSalle INT,
    planSalle BLOB,
    dimensionOuverture float,
    dimensionProfondeur float,
    lieuID INT,
    FOREIGN KEY (lieuID) REFERENCES LIEU(lieuID),

);

CREATE TABLE SALLETYPEPLACE(
    typeId INT PRIMARY KEY,
    salleID INT PRIMARY KEY,
    capacite INT,
    FOREIGN KEY (typeId) REFERENCES TYPEPLACE(typeId),
    FOREIGN KEY (salleID) REFERENCES SALLE(salleID)

)
-- Table pour stocker les informations sur l'hebergement
CREATE TABLE HEBERGMENT (
    hebergementID INT PRIMARY KEY AUTO_INCREMENT,
    nomHebergement VARCHAR(255) NOT NULL,
    capacitéH INT NOT NULL,
    qualitéH INT NOT NULL
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
    adresseN VARCHAR(255),
    numSecuriteSociale INT,
    numCNI INT,
    dateDelivranceCNI DATE,
    dateExpirationCNI DATE
);



CREATE TABLE VEHICULE(
    immatriculation VARCHAR(255) PRIMARY KEY,
    typeVehicule VARCHAR(255),
    capacitéV INT
);

-- Table pour stocker les informations sur les concerts
CREATE TABLE CONCERT (
    concertId INT PRIMARY KEY,
    dateHeureDebutConcert DATETIME,
    dureeConcert INT,
    lieuId INT,
    festivalId INT,
    groupeId INT,
    FOREIGN KEY (lieuId) REFERENCES LIEU(lieuId),

); 

create Table MATERIEL(
    materielID int PRIMARY KEY,
    nomMateriel VARCHAR(255)
);

create Table NECESSITER(
    materielID int PRIMARY KEY,
    concertID int PRIMARY KEY,
    quantiteM int ,
    FOREIGN KEY (materielID) REFERENCES MATERIEL(materielID),
    FOREIGN KEY (concertID) REFERENCES CONCERT(concertID)
);

create Table MATERIELSALLE(
    materielSalleID int PRIMARY KEY,
    salleID INT,
    nomMaterielS VARCHAR(255),
    disponible BOOLEAN,
    FOREIGN KEY (salleID) REFERENCES SALLE(salleID)

);




