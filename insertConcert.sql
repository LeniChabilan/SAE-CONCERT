INSERT INTO MUSICIEN (musicienID, nomMusicien)VALUES
  (1, 'Pierre Dupont'),
  (2, 'Élise Martin'),
  (3, 'Claude Leblanc'),
  (4, 'Camille Dubois'),
  (5, 'Lucien Lambert');

INSERT INTO MATERIELARTISTE (materielArtisteID, nomMaterielArt, disponible)VALUES
  (1, 'Guitare acoustique', true),
  (2, 'Piano à queue', true),
  (3, 'Batterie complète', false),
  (4, 'Saxophone alto', true),
  (5, 'Violoncelle', true);


INSERT INTO ROLEP (roleID, nomRole)VALUES
  (1, 'Ingénieur du son'),
  (2, 'Éclairagiste'),
  (3, 'Régisseur de scène'),
  (4, 'Technicien de son'),
  (5, 'Technicien éclairage');


INSERT INTO ORGANISATION (nomOrga, motDePasse, typeOrga)VALUES
  ('HarmonieMusicale', 'mdp123', 'Technique'),
  ('BienveillanceArtistique', 'mdp123', 'Bien-être des Artistes'),
  ('SonsEnScène', 'mdp123', 'Technique'),
  ('CoeurDeScene', 'mdp123', 'Bien-être des Artistes');


INSERT INTO TYPEPLACE (typePlaceID, nomPlace, descriptionP)VALUES
  (1, 'VIP', 'Accès privilégié avec vue exceptionnelle sur la scène.'),
  (2, 'Place Asise', 'Des sièges confortables et une bonne vue sur la scène.'),
  (3, 'Place en Fosse', 'Directement dans la fosse du concert'),
  (4, 'Place Debout', 'Accès à la zone debout pour ceux qui aiment danser.'),
  (5, 'Place Enfant', 'Pour les jeunes fans et enfants (âge limite : 12 ans)'),
  (6, 'Place pour Personnes à Mobilité Réduite', 'Places spécialement aménagées pour les personnes à mobilité réduite.');


INSERT INTO LIEU (lieuID, nomVille, adresseL, departement)VALUES
  (1, 'Lyon', 'Salle Harmonie', 69001),
  (2, 'Lyon', 'Palais des Arts', 69002),
  (3, 'Lyon', 'La Cité Musicale', 69003),
  (4, 'Lyon', 'Salle des Artistes', 69004),
  (5, 'Lyon', 'Le Centre de Musique', 69005),
  (6, 'Lyon', 'Salle Étoile', 69006),
  (7, 'Lyon', 'Le Forum Musical', 69007);


INSERT INTO ARTISTE (artisteID, pseudoArtiste, nomA, prenomA, mailA, DdNA, LdN, adresseA, numSecuriteSociale, numCNI, dateDelivranceCNI, dateExpirationCNI, dansGroupe)VALUES
  (1, 'RockStar123', 'Dupont', 'Jean', 'jean.dupont@gmail.com', '1990-05-15', 'Lyon', '123 Rue de la Musique', 12367890, 456, '2005-06-20', '2025-06-20', TRUE),
  (2, 'GrooveMaster', 'Martin', 'Marie', 'marie.martin@gmail.com', '1985-08-25', 'Lyon', '456 Avenue du Spectacle', 78954321, 987, '2003-04-12', '2023-04-12', TRUE),
  (3, 'JazzCat', 'Lefebvre', 'Paul', 'paul.lefebvre@gmail.com', '1993-03-10', 'Lyon', '789 Boulevard du Son', 23454321, 567, '2010-09-05', '2030-09-05', TRUE),
  (4, 'PopPrincess', 'Dubois', 'Sophie', 'sophie.dubois@gmail.com', '1988-11-03', 'Lyon', '321 Rue des Artistes', 89045678, 654, '2006-07-15', '2026-07-15', FALSE),
  (5, 'MetalHead', 'Bertrand', 'Luc', 'luc.bertrand@gmail.com', '1997-02-17', 'Lyon', '567 Avenue du Rock', 43245678, 123, '2008-12-01', '2028-12-01', TRUE),
  (6, 'BluesMaestro', 'Roux', 'Alice', 'alice.roux@gmail.com', '1980-07-08', 'Lyon', '234 Boulevard du Blues', 76554321, 365, '2001-03-30', '2021-03-30', TRUE),
  (7, 'ReggaeVibes', 'Girard', 'Hugo', 'hugo.girard@gmail.com', '1995-09-27', 'Lyon', '987 Rue de la Reggae', 32198765, 542, '2007-11-22', '2027-11-22', TRUE),
  (8, 'ClassicalMaestro', 'Fournier', 'Emma', 'emma.fournier@gmail.com', '1983-04-02', 'Lyon', '678 Avenue des Classiques', 23498765, 765, '2004-08-10', '2024-08-10', TRUE),
  (9, 'IndieSinger', 'Petit', 'Lucas', 'lucas.petit@gmail.com', '1992-12-19', 'Lyon', '345 Rue de Indépendance', 54354321, 876, '2009-06-18', '2029-06-18', FALSE),
  (10, 'FolkFiddler', 'Moreau', 'Anna', 'anna.moreau@gmail.com', '1998-06-23', 'Lyon', '234 Avenue de la Folk', 87654321, 345, '2011-05-02', '2031-05-02', TRUE);

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
  ('EF-120-GH', 'Minibus', 15);

INSERT INTO MATERIEL (materielID, nomMateriel)VALUES
  (1, 'Microphone dynamique'),
  (2, 'Microphone à condensateur'),
  (3, 'Table de mixage 8 canaux'),
  (4, 'Table de mixage 16 canaux'),
  (5, 'Table de mixage numérique'),
  (6, 'Enceinte passive 12'),
  (7, 'Enceinte passive 15'),
  (8, 'Enceinte active 10'),
  (9, 'Enceinte active 18'),
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
  (38, 'Écran de projection 120'),
  (39, 'Écran LED 55'),
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
  (69, 'Écran de projection électrique 150'),
  (70, 'Lyre à LED wash 250W'),
  (71, 'Console éclairage à gradateurs'),
  (72, 'Machine à confettis électrique'),
  (73, 'Enceinte passive 10'),
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
  (84, 'Écran LED 75'),
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
  (98, 'Écran de projection motorisé 200'),
  (99, 'Lyre beam 200W'),
  (100, 'Lyre wash 180W'),
  (101, 'Console de mixage compacte 12 canaux'),
  (102, 'Enceinte active 8'),
  (103, 'Caisse de régie avec rack'),
  (104, 'Microphone dynamique instrument'),
  (105, 'Machine à confettis manuelle'),
  (106, 'Ampli casque 12 canaux'),
  (107, 'Écran LED 85'),
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
  (123, 'Écran de projection électrique 250'),
  (124, 'Lyre spot wash 180W'),
  (125, 'Console de mixage numérique 64 canaux'),
  (126, 'Lyre à LED beam spot 400W'),
  (127, 'Machine à mousse professionnelle'),
  (128, 'Enceinte passive 15'),
  (129, 'Ampli casque 24 canaux'),
  (130, 'Microphone studio à ruban'),
  (131, 'Câble alimentation PowerCON TRUE1'),
  (132, 'Pied éclairage télescopique à treuil'),
  (133, 'Lyre à LED spot beam 250W'),
  (134, 'Machine à brouillard haute densité professionnelle'),
  (135, 'Console de mixage analogique 48 canaux'),
  (136, 'Écran LED 100'),
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
  (148, 'Enceinte active 12'),
  (149, 'Lyre à LED wash spot beam 500W'),
  (150, 'Machine à mousse lourde professionnelle');


INSERT INTO GROUPE (groupeID, nomGroupe)VALUES
  (1, 'Les Rockeurs'),
  (2, 'PopPrincess'),
  (3, 'Pop Sensation'),
  (4, 'IndieSinger');


INSERT INTO SALLE (salleID, nomSalle, capaciteTotaleSalle, planSalle, dimensionOuverture, dimensionProfondeur, lieuID)VALUES
  (1, 'Salle A', 500, NULL, 20.5, 30.2, 1), -- Lieu ID 1 (Lyon Salle 1)
  (2, 'Salle B', 300, NULL, 15.8, 25.4, 2), -- Lieu ID 2 (Lyon Salle 2)
  (3, 'Salle C', 700, NULL, 25.0, 35.6, 3), -- Lieu ID 3 (Lyon Salle 3)
  (4, 'Salle D', 400, NULL, 18.2, 27.9, 4); -- Lieu ID 4 (Lyon Salle 4)


INSERT INTO PERSONELTECHNIQUE(personelTechniqueID, roleID, nomP, prenomP)VALUES
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

INSERT INTO PLAN (planID, planScene, planFeu, salleID)VALUES
  (1, NULL, NULL, 1),
  (2, NULL, NULL, 2),
  (3, NULL, NULL, 3),
  (4, NULL, NULL, 4),
  (5, NULL, NULL, 1),
  (6, NULL, NULL, 2),
  (7, NULL, NULL, 3),
  (8, NULL, NULL, 4);

INSERT INTO HEBERGMENT (hebergementID, nomHebergement, capacitéH, qualitéH, lieuID, prix)VALUES
  (1, 'Hôtel de Lyon', 100, 4, 1, 150),
  (2, 'Auberge des Musiciens', 50, 3, 2, 80),
  (3, 'Appartement du Vieux Lyon', 30, 5, 1, 120),
  (4, 'Chambre d hôtes du Vieux Lyon', 10, 4, 1, 70),
  (5, 'Hôtel Belle Vue', 80, 4, 3, 130),
  (6, 'Maison de Ville Lumière', 45, 3, 2, 90);

INSERT INTO MATERIELSALLE (materielSalleID, salleID, nomMaterielS, disponible)VALUES
  (1, 1, 'Microphone dynamique', true),
  (2, 1, 'Microphone à condensateur', true),
  (3, 1, 'Table de mixage 8 canaux', true),
  (4, 1, 'Table de mixage 16 canaux', false),
  (5, 1, 'Table de mixage numérique', true),
  (6, 2, 'Enceinte passive 12', true),
  (7, 2, 'Enceinte passive 15', false),
  (8, 2, 'Enceinte active 10', true),
  (9, 2, 'Enceinte active 18', true),
  (10, 2, 'Amplificateur de puissance 1000W', true),
  (11, 3, 'Amplificateur de puissance 2000W', true),
  (12, 3, 'Amplificateur de casque', false),
  (13, 3, 'Casque écoute professionnel', true),
  (14, 3, 'Effets audio rackables', true),
  (15, 3, 'Laser RGB 1W', false),
  (16, 4, 'Projecteur LED 100W', true),
  (17, 4, 'Projecteur LED 200W', true),
  (18, 4, 'Machine à brouillard', true),
  (19, 4, 'Machine à fumée lourde', false),
  (20, 4, 'Lyre à LED 60W', true);



INSERT INTO CONCERT (concertID, nomConcert, dateDebutConcert, dateFinConcert, ficheTechnique, catering, salleID, groupeID) VALUES
  (1, 'Concert 1', '2023-11-28', '2023-11-29', 'Fiche technique du concert 1', 'Catering du concert 1', 2, 2),
  (2, 'Concert 2', '2023-11-27', '2023-11-28', 'Fiche technique du concert 2', 'Catering du concert 2', 3, 1),
  (3, 'Concert 3', '2023-12-23', '2023-12-24', 'Fiche technique du concert 3', 'Catering du concert 3', 1, 3);


INSERT INTO MUSICIENADDITIONEL(musicienID, concertID)VALUES
  (1, 1), 
  (2, 1), 
  (3, 1), 
  (4, 2), 
  (5, 2), 
  (4, 3), 
  (1, 3); 

INSERT INTO TRANSPORTE (concertID, immatriculation)VALUES
  (1, 'AB-123-CD'),
  (2, 'EF-123-GH'),
  (3, 'CD-123-EF');


INSERT INTO COMPOSER (artisteID, groupeID)VALUES
  (1, 1), 
  (2, 1),
  (3, 1),
  (4, 2), 
  (9, 4), 
  (7, 3), 
  (5, 3); 


INSERT INTO NECESSITER (materielID, concertID)VALUES
  (1, 1), 
  (2, 1),
  (3, 2), 
  (4, 2),
  (5, 2), 
  (6, 2), 
  (7, 2), 
  (8, 2), 
  (9, 2), 
  (10, 1), 
  (11, 1), 
  (12, 1), 
  (13, 1), 
  (14, 1), 
  (15, 1), 
  (16, 1), 
  (17, 1), 
  (18, 1), 
  (19, 1), 
  (20, 1), 
  (21, 1), 
  (22, 1), 
  (23, 1), 
  (24, 1), 
  (25, 2), 
  (26, 2), 
  (27, 2), 
  (28, 2), 
  (29, 2), 
  (30, 2), 
  (31, 2), 
  (32, 2), 
  (33, 2), 
  (34, 2), 
  (35, 2), 
  (36, 2), 
  (37, 2), 
  (38, 2), 
  (39, 2), 
  (40, 3), 
  (41, 3), 
  (42, 3), 
  (43, 3), 
  (44, 3), 
  (45, 3), 
  (46, 3), 
  (47, 3), 
  (48, 3), 
  (49, 3), 
  (50, 3), 
  (51, 3), 
  (52, 3), 
  (53, 3), 
  (54, 3), 
  (55, 3), 
  (56, 3), 
  (57, 3), 
  (58, 3), 
  (59, 3);
  
INSERT INTO UTILISE (materielArtisteID, groupeID, quantiteMaterielArt)
VALUES
  (1, 1, 2),  -- Les Rockeurs utilisent 2 guitares acoustiques
  (2, 2, 1),  -- PopPrincess utilise 1 piano à queue
  (3, 1, 1),  -- Les Rockeurs utilisent 1 batterie complète
  (4, 3, 3),  -- Pop Sensation utilise 3 saxophones alto
  (5, 4, 2);  -- IndieSinger utilise 2 violoncelles


INSERT INTO PARTICIPE (concertId, groupeID)VALUES
  (1, 1), -- Groupe ID 1 participe au Concert ID 1
  (2, 2), -- Groupe ID 2 participe au Concert ID 2
  (3, 3); -- Groupe ID 3 participe au Concert ID 3



INSERT INTO PREPARE (personelTechniqueID, concertID)VALUES
  (1, 1),  -- Martin Dupont prépare Concert 1
  (2, 1),  -- Sophie Lefebvre prépare Concert 1
  (3, 1),  -- Philippe Roux prépare Concert 1
  (4, 2),  -- Camille Moreau prépare Concert 2
  (5, 2),  -- Éric Lambert prépare Concert 2
  (6, 3),  -- Isabelle Gagnon prépare Concert 3
  (7, 3),  -- Antoine Lapointe prépare Concert 3
  (8, 3),  -- David Bergeron prépare Concert 3
  (9, 1),  -- Valérie Leclerc prépare Concert 1
  (10, 1), -- Sophie Tremblay prépare Concert 1
  (11, 2), -- Thomas Leroy prépare Concert 2
  (12, 3); -- Léa Dubois prépare Concert 3


INSERT INTO SALLETYPEPLACE (typePlaceID, salleID, capaciteS)
VALUES
  (1, 1, 50),  -- Capacité VIP dans Salle A
  (2, 1, 200),  -- Capacité Place Assise dans Salle A
  (3, 1, 300),  -- Capacité Place en Fosse dans Salle A
  (4, 1, 400),  -- Capacité Place Debout dans Salle A
  (5, 1, 30),  -- Capacité Place Enfant dans Salle A
  (6, 1, 10),  -- Capacité Place pour Personnes à Mobilité Réduite dans Salle A

  (1, 2, 30),  -- Capacité VIP dans Salle B
  (2, 2, 150),  -- Capacité Place Assise dans Salle B
  (3, 2, 200),  -- Capacité Place en Fosse dans Salle B
  (4, 2, 250),  -- Capacité Place Debout dans Salle B
  (5, 2, 20),  -- Capacité Place Enfant dans Salle B
  (6, 2, 8),  -- Capacité Place pour Personnes à Mobilité Réduite dans Salle B

  (1, 3, 70),  -- Capacité VIP dans Salle C
  (2, 3, 350),  -- Capacité Place Assise dans Salle C
  (3, 3, 450),  -- Capacité Place en Fosse dans Salle C
  (4, 3, 600),  -- Capacité Place Debout dans Salle C
  (5, 3, 40),  -- Capacité Place Enfant dans Salle C
  (6, 3, 12),  -- Capacité Place pour Personnes à Mobilité Réduite dans Salle C

  (1, 4, 40),  -- Capacité VIP dans Salle D
  (2, 4, 200),  -- Capacité Place Assise dans Salle D
  (3, 4, 250),  -- Capacité Place en Fosse dans Salle D
  (4, 4, 300),  -- Capacité Place Debout dans Salle D
  (5, 4, 25),  -- Capacité Place Enfant dans Salle D
  (6, 4, 6);  -- Capacité Place pour Personnes à Mobilité Réduite dans Salle D


INSERT INTO ORGANISER (concertID, nomOrga) VALUES
  (1, 'HarmonieMusicale'), 
  (1, 'BienveillanceArtistique'), 
  (2, 'SonsEnScène'),
  (2, 'CoeurDeScene'), 
  (3, 'HarmonieMusicale'),
  (3, 'CoeurDeScene');

