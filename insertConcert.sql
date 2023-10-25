-- Exemple d'insertion de musiciens
INSERT INTO MUSICIEN (musicienID, nomMusicien)VALUES
  (1, 'Pierre Dupont'),
  (2, 'Élise Martin'),
  (3, 'Claude Leblanc'),
  (4, 'Camille Dubois'),
  (5, 'Lucien Lambert');

-- Exemple d'insertion de matériel artiste (instruments de musique)
INSERT INTO MATERIELARTISTE (materielArtisteID, nomMaterielArt, disponible)VALUES
  (1, 'Guitare acoustique', true),
  (2, 'Piano à queue', true),
  (3, 'Batterie complète', false),
  (4, 'Saxophone alto', true),
  (5, 'Violoncelle', true);


-- Insertion de rôles pour le personnel technique
INSERT INTO ROLEP (roleID, nomRole)VALUES
  (1, 'Ingénieur du son'),
  (2, 'Éclairagiste'),
  (3, 'Régisseur de scène'),
  (4, 'Technicien de son'),
  (5, 'Technicien éclairage'),


-- Insertion d'organisations fictives
INSERT INTO ORGANISATION (nomOrga, motDePasse, typeOrga)VALUES
  ('HarmonieMusicale', 'mdp123', 'Technique'),
  ('BienveillanceArtistique', 'mdp123', 'Bien-être des Artistes'),
  ('SonsEnScène', 'mdp123', 'Technique'),
  ('CoeurDeScene', 'mdp123', 'Bien-être des Artistes'),


-- Insertion de différents types de places
INSERT INTO TYPEPLACE (typePlaceID, nomPlace, descriptionP)VALUES
  (1, 'VIP', 'Accès privilégié avec vue exceptionnelle sur la scène.'),
  (2, 'Place Asise', 'Des sièges confortables et une bonne vue sur la scène.'),
  (3, 'Place en Fosse', 'Directement dans la fosse du concert'),
  (4, 'Place Debout', 'Accès à la zone debout pour ceux qui aiment danser.'),
  (5, 'Place Enfant', 'Pour les jeunes fans et enfants (âge limite : 12 ans)'),
  (6, 'Place pour Personnes à Mobilité Réduite', 'Places spécialement aménagées pour les personnes à mobilité réduite.');


-- Insertion de salles de concert fictives situées à Lyon
INSERT INTO LIEU (lieuID, nomVille, adresseL, departement)VALUES
  (1, 'Lyon', 'Salle Harmonie', 69001),
  (2, 'Lyon', 'Palais des Arts', 69002),
  (3, 'Lyon', 'La Cité Musicale', 69003),
  (4, 'Lyon', 'Salle des Artistes', 69004),
  (5, 'Lyon', 'Le Centre de Musique', 69005),
  (6, 'Lyon', 'Salle Étoile', 69006),
  (7, 'Lyon', 'Le Forum Musical', 69007);


-- Insertion d'artistes fictifs avec numéros aléatoires
INSERT INTO ARTISTE (artisteID, pseudoArtiste, nomA, prenomA, mailA, DdNA, LdN, adresseA, numSecuriteSociale, numCNI, dateDelivranceCNI, dateExpirationCNI, dansGroupe)VALUES
  (1, 'RockStar123', 'Dupont', 'Jean', 'jean.dupont@gmail.com', '1990-05-15', 'Lyon', '123 Rue de la Musique', 12367890, 456, '2005-06-20', '2025-06-20', TRUE),
  (2, 'GrooveMaster', 'Martin', 'Marie', 'marie.martin@gmail.com', '1985-08-25', 'Lyon', '456 Avenue du Spectacle', 78954321, 987, '2003-04-12', '2023-04-12', TRUE),
  (3, 'JazzCat', 'Lefebvre', 'Paul', 'paul.lefebvre@gmail.com', '1993-03-10', 'Lyon', '789 Boulevard du Son', 23454321, 567, '2010-09-05', '2030-09-05', TRUE),
  (4, 'PopPrincess', 'Dubois', 'Sophie', 'sophie.dubois@gmail.com', '1988-11-03', 'Lyon', '321 Rue des Artistes', 89045678, 654, '2006-07-15', '2026-07-15', FALSE),
  (5, 'MetalHead', 'Bertrand', 'Luc', 'luc.bertrand@gmail.com', '1997-02-17', 'Lyon', '567 Avenue du Rock', 43245678, 123, '2008-12-01', '2028-12-01', TRUE),
  (6, 'BluesMaestro', 'Roux', 'Alice', 'alice.roux@gmail.com', '1980-07-08', 'Lyon', '234 Boulevard du Blues', 76554321, 876, '2001-03-30', '2021-03-30', TRUE),
  (7, 'ReggaeVibes', 'Girard', 'Hugo', 'hugo.girard@gmail.com', '1995-09-27', 'Lyon', '987 Rue de la Reggae', 32198765, 987, '2007-11-22', '2027-11-22', TRUE),
  (8, 'ClassicalMaestro', 'Fournier', 'Emma', 'emma.fournier@gmail.com', '1983-04-02', 'Lyon', '678 Avenue des Classiques', 23498765, 765, '2004-08-10', '2024-08-10', TRUE),
  (9, 'IndieSinger', 'Petit', 'Lucas', 'lucas.petit@gmail.com', '1992-12-19', 'Lyon', '345 Rue de Indépendance', 54354321, 876, '2009-06-18', '2029-06-18', FALSE),
  (10, 'FolkFiddler', 'Moreau', 'Anna', 'anna.moreau@gmail.com', '1998-06-23', 'Lyon', '234 Avenue de la Folk', 87654321, 345, '2011-05-02', '2031-05-02', TRUE),
  (11, 'ElectronicBeats', 'Roy', 'Léa', 'lea.roy@gmail.com', '1989-10-12', 'Lyon', '789 Rue de lÉlectronique', 99998765, 111, '2002-02-28', '2022-02-28', TRUE),
  (12, 'SoulSinger', 'Garcia', 'Enzo', 'enzo.garcia@gmail.com', '1991-07-07', 'Lyon', '456 Boulevard de la Soul', 22298765, 333, '2000-10-05', '2020-10-05', TRUE),
  (13, 'PunkRocker', 'Lévesque', 'Zoé', 'zoe.levesque@gmail.com', '1987-01-31', 'Lyon', '123 Avenue du Punk', 45654321, 999, '2000-02-15', '2020-02-15', TRUE),
  (14, 'CountryCowboy', 'Perrin', 'Léo', 'leo.perrin@gmail.com', '1996-04-14', 'Lyon', '321 Rue du Country', 55598765, 777, '2013-07-12', '2033-07-12', FALSE),
  (15, 'RapMaster', 'Mallet', 'Eva', 'eva.mallet@gmail.com', '1986-03-05', 'Lyon', '567 Boulevard du Rap', 77798765, 555, '2000-02-15', '2020-02-15', TRUE);

-- Insertion de véhicules fictifs
INSERT INTO VEHICULE (immatriculation, typeVehicule, capacitéV)VALUES
  ('AB-123-CD', 'Voiture', 5),
  ('XY-789-ZW', 'Camion', 10),
  ('LM-456-OP', 'Moto', 2),
  ('EF-123-GH', 'Voiture', 7),
  ('JK-789-LM', 'Voiture', 5),
  ('UV-456-WX', 'Camion', 10),
  ('CD-123-EF', 'Moto', 2),
  ('GH-789-IJ', 'Fourgon', 8),
  ('OP-456-QR', 'Bus', 35),
  ('LM-123-UV', 'Minibus', 15),
  ('WX-789-CD', 'Bus', 50),
  ('EF-123-GH', 'Minibus', 15);

-- Insertion de matériel fictif pour le son et la lumière
INSERT INTO MATERIEL (materielID, nomMateriel)VALUES
  (1, 'Microphone dynamique'),
  (2, 'Microphone à condensateur'),
  (3, 'Table de mixage 8 canaux'),
  (4, 'Table de mixage 16 canaux'),
  (5, 'Table de mixage numérique'),
  (6, 'Enceinte passive 12"'),
  (7, 'Enceinte passive 15"'),
  (8, 'Enceinte active 10"'),
  (9, 'Enceinte active 18"'),
  (10, 'Amplificateur de puissance 1000W'),
  (11, 'Amplificateur de puissance 2000W'),
  (12, 'Amplificateur de casque'),
  (13, 'Casque écoute professionnel'),
  (14, 'Effets audio rackables'),
  (15, 'Laser RGB 1W'),
  (16, 'Projecteur LED 100W'),
  (17, 'Projecteur LED 200W'),
  (18, 'Machine à brouillard'),
  (19, 'Machine à fumée lourde'),
  (20, 'Lyre à LED 60W'),
  (21, 'Lyre à LED 150W'),
  (22, 'Pied de micro droit'),
  (23, 'Pied de micro perche'),
  (24, 'Câble XLR 3m'),
  (25, 'Câble XLR 5m'),
  (26, 'Câble jack 6.35mm 10m'),
  (27, 'Câble speakon 25m'),
  (28, 'Égaliseur graphique 31 bandes'),
  (29, 'Égaliseur paramétrique'),
  (30, 'Console éclairage DMX 512'),
  (31, 'Machine à bulles'),
  (32, 'Machine à neige'),
  (33, 'Machine à confettis'),
  (34, 'Machine à mousse'),
  (35, 'Stroboscope 1000W'),
  (36, 'Stroboscope LED'),
  (37, 'Panneau LED 4x4'),
  (38, 'Écran de projection 120"'),
  (39, 'Écran LED 55"'),
  (40, 'Ampli casque 4 canaux'),
  (41, 'Caisse de régie'),
  (42, 'Console de mixage numérique 24 canaux'),
  (43, 'Microphone sans fil main'),
  (44, 'Microphone sans fil cravate'),
  (45, 'Microphone sans fil serre-tête'),
  (46, 'Ampli de puissance 4000W'),
  (47, 'Lyre à LED 250W'),
  (48, 'Éclairage UV 400W'),
  (49, 'Machine à brouillard lourd'),
  (50, 'Lyre laser 1W'),
  (51, 'Ampli casque 8 canaux'),
  (52, 'Lyre spot 75W'),
  (53, 'Lyre wash 120W'),
  (54, 'Console de mixage analogique 32 canaux'),
  (55, 'Effets audio DSP'),
  (56, 'Enceinte colonne active 1000W'),
  (57, 'Console éclairage compacte'),
  (58, 'Machine à bulles géante'),
  (59, 'Lyre beam 150W'),
  (60, 'Machine à neige lourde'),
  (61, 'Microphone chant studio'),
  (62, 'Microphone overhead studio'),
  (63, 'Microphone batterie studio'),
  (64, 'Table de mixage compacte 6 canaux'),
  (65, 'Lyre à LED 300W'),
  (66, 'Projecteur LED 400W'),
  (67, 'Stroboscope 1500W'),
  (68, 'Machine à brouillard professionnel'),
  (69, 'Écran de projection électrique 150"'),
  (70, 'Lyre à LED wash 250W'),
  (71, 'Console éclairage à gradateurs'),
  (72, 'Machine à confettis électrique'),
  (73, 'Enceinte passive 10"'),
  (74, 'Ampli casque 16 canaux'),
  (75, 'Microphone chant dynamique'),
  (76, 'Câble alimentation PowerCON'),
  (77, 'Pied éclairage télescopique'),
  (78, 'Câble DMX 5m'),
  (79, 'Lyre spot 120W'),
  (80, 'Machine à fumée basse densité'),
  (81, 'Table de mixage 32 canaux'),
  (82, 'Microphone à ruban'),
  (83, 'Machine à neige artificielle'),
  (84, 'Écran LED 75"'),
  (85, 'Amplificateur de casque 8 canaux'),
  (86, 'Console de mixage numérique 48 canaux'),
  (87, 'Machine à fumée lourde professionnelle'),
  (88, 'Lyre laser RGB 2W'),
  (89, 'Lyre à LED 400W'),
  (90, 'Égaliseur 15 bandes'),
  (91, 'Machine à bulles professionnelle'),
  (92, 'Lyre à LED spot 200W'),
  (93, 'Machine à mousse compacte'),
  (94, 'Console de mixage analogique 16 canaux'),
  (95, 'Câble jack 3.5mm 3m'),
  (96, 'Câble adaptateur XLR-jack 6.35mm'),
  (97, 'Câble speakon 50m'),
  (98, 'Écran de projection motorisé 200"'),
  (99, 'Lyre beam 200W'),
  (100, 'Lyre wash 180W'),
  (101, 'Console de mixage compacte 12 canaux'),
  (102, 'Enceinte active 8"'),
  (103, 'Caisse de régie avec rack'),
  (104, 'Microphone dynamique instrument'),
  (105, 'Machine à confettis manuelle'),
  (106, 'Ampli casque 12 canaux'),
  (107, 'Écran LED 85"'),
  (108, 'Lyre à LED wash spot 350W'),
  (109, 'Machine à brouillard lourd professionnelle'),
  (110, 'Table de mixage 24 canaux'),
  (111, 'Lyre à LED hybride 280W'),
  (112, 'Machine à neige professionnelle'),
  (113, 'Microphone cravate sans fil'),
  (114, 'Lyre à LED wash 300W'),
  (115, 'Projecteur LED 800W'),
  (116, 'Machine à confettis électrique à gros débit'),
  (117, 'Stroboscope LED 500W'),
  (118, 'Machine à fumée basse densité professionnelle'),
  (119, 'Câble DMX 10m'),
  (120, 'Console éclairage à gradateurs 48 canaux'),
  (121, 'Lyre à LED wash beam 350W'),
  (122, 'Ampli de puissance 5000W'),
  (123, 'Écran de projection électrique 250"'),
  (124, 'Lyre spot wash 180W'),
  (125, 'Console de mixage numérique 64 canaux'),
  (126, 'Lyre à LED beam spot 400W'),
  (127, 'Machine à mousse professionnelle'),
  (128, 'Enceinte passive 15"'),
  (129, 'Ampli casque 24 canaux'),
  (130, 'Microphone studio à ruban'),
  (131, 'Câble alimentation PowerCON TRUE1'),
  (132, 'Pied éclairage télescopique à treuil'),
  (133, 'Lyre à LED spot beam 250W'),
  (134, 'Machine à brouillard haute densité professionnelle'),
  (135, 'Console de mixage analogique 48 canaux'),
  (136, 'Écran LED 100"'),
  (137, 'Amplificateur de casque 16 canaux'),
  (138, 'Machine à confettis électrique à grande capacité'),
  (139, 'Lyre laser RGB 4W'),
  (140, 'Machine à brouillard à jet continu'),
  (141, 'Table de mixage 48 canaux'),
  (142, 'Microphone studio à condensateur'),
  (143, 'Machine à neige professionnelle à gros débit'),
  (144, 'Caisse de régie avec rack et roulettes'),
  (145, 'Lyre à LED spot wash beam 350W'),
  (146, 'Machine à fumée basse densité professionnelle avec télécommande'),
  (147, 'Console de mixage compacte 16 canaux'),
  (148, 'Enceinte active 12"'),
  (149, 'Lyre à LED wash spot beam 500W'),
  (150, 'Machine à mousse lourde professionnelle');


INSERT INTO GROUPE (groupeID, nomGroupe)VALUES
  (1, 'Les Rockeurs'),
  (2, 'PopPrincess'),
  (3, 'Pop Sensation'),
  (4, 'IndieSinger'),
  (5, 'Heavy Metal Legends'),
  (6, 'CountryCowboy'),

-- Insertion de salles fictives
INSERT INTO SALLE (salleID, nomSalle, capaciteTotaleSalle, planSalle, dimensionOuverture, dimensionProfondeur, lieuID)VALUES
  (1, 'Salle A', 500, NULL, 20.5, 30.2, 1), -- Lieu ID 1 (Lyon Salle 1)
  (2, 'Salle B', 300, NULL, 15.8, 25.4, 2), -- Lieu ID 2 (Lyon Salle 2)
  (3, 'Salle C', 700, NULL, 25.0, 35.6, 3), -- Lieu ID 3 (Lyon Salle 3)
  (4, 'Salle D', 400, NULL, 18.2, 27.9, 4), -- Lieu ID 4 (Lyon Salle 4)
  (5, 'Salle E', 250, NULL, 12.6, 22.1, 5); -- Lieu ID 5 (Lyon Salle 5)
  (6, 'Salle F', 450, NULL, 17.3, 28.7, 6), -- Lieu ID 6 (Lyon Salle 6)
  (7, 'Salle G', 550, NULL, 19.9, 32.1, 7), -- Lieu ID 7 (Lyon Salle 7)

  -- Insertion de membres du personnel technique fictifs
INSERT INTO PERSONNELTECHNIQUE (personelTechniqueID, roleID, nomP, prenomP)VALUES
  (1, 1, 'Martin', 'Dupont'), -- Ingénieur du son
  (2, 2, 'Sophie', 'Lefebvre'), -- Éclairagiste
  (3, 3, 'Philippe', 'Roux'), -- Régisseur de scène
  (4, 4, 'Camille', 'Moreau'), -- Technicien de son
  (5, 5, 'Éric', 'Lambert'), -- Technicien éclairage
  (6, 1, 'Isabelle', 'Gagnon'), -- Ingénieur du son
  (7, 2, 'Antoine', 'Lapointe'), -- Éclairagiste
  (8, 3, 'David', 'Bergeron'), -- Régisseur de scène
  (9, 4, 'Valérie', 'Leclerc'), -- Technicien de son
  (10, 5, 'Sophie', 'Tremblay'), -- Technicien éclairage
  (11, 1, 'Thomas', 'Leroy'), -- Ingénieur du son
  (12, 2, 'Léa', 'Dubois'); -- Éclairagiste
