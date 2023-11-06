import click
from .app import app,db
from datetime import datetime

@app.cli.command()
@click.argument('filename')






def loaddb(filename):
    '''Crée les tables et les remplit de données'''
    db.create_all()
    import yaml
    data = yaml.safe_load(open(filename))
    from .models import Musicien, MaterielArtiste, RoleP, Organisation, TypePlace, Lieu, Artiste, Vehicule, Materiel, Groupe, Salle, PersonelTechnique, Plan, Hebergement, MaterielSalle, Concert, MusicienAdditionnel, Transporte, Necessiter, Composer, Utilise, Participe, Prepare, SalleTypePlace, Organiser

    for nomTable in data:
        if "Musicien" in nomTable:
            musiciens = nomTable["Musicien"]
            for musicien_data in musiciens:
                musicien = Musicien(musicienID=musicien_data["musicienID"], nomMusicien=musicien_data["nomMusicien"])
                db.session.add(musicien)

        if "MaterielArtiste" in nomTable:
            materiels = nomTable["MaterielArtiste"]
            for materiel_data in materiels:
                materiel = MaterielArtiste(materielArtisteID=materiel_data["materielArtisteID"], nomMaterielArt=materiel_data["nomMaterielArt"], disponible=materiel_data["disponible"])
                db.session.add(materiel)

        if "RoleP" in nomTable:
            roles = nomTable["RoleP"]
            for role_data in roles:
                role = RoleP(roleID=role_data["roleID"], nomRole=role_data["nomRole"])
                db.session.add(role)

        if "Organisation" in nomTable:
            organisations = nomTable["Organisation"]
            for organisation_data in organisations:
                organisation = Organisation(nomOrga=organisation_data["nomOrga"], motDePasse=organisation_data["motDePasse"], typeOrga=organisation_data["typeOrga"])
                db.session.add(organisation)

        if "TypePlace" in nomTable:
            typePlaces = nomTable["TypePlace"]
            for typePlace_data in typePlaces:
                typePlace = TypePlace(typePlaceID=typePlace_data["typePlaceID"], nomPlace=typePlace_data["nomPlace"], descriptionP=typePlace_data["descriptionP"])
                db.session.add(typePlace)

        if "Lieu" in nomTable:
            lieux = nomTable["Lieu"]
            for lieu_data in lieux:
                lieu = Lieu(lieuID=lieu_data["lieuID"], nomVille=lieu_data["nomVille"], adresseL=lieu_data["adresseL"], departement=lieu_data["departement"])
                db.session.add(lieu)

        if "Artiste" in nomTable:
            artistes = nomTable["Artiste"]
            for artiste_data in artistes:
                artiste = Artiste(artisteID=artiste_data["artisteID"], pseudoArtiste=artiste_data["pseudoArtiste"], nomA=artiste_data["nomA"], prenomA=artiste_data["prenomA"],mailA=artiste_data["mailA"], DdNA=datetime.strptime(artiste_data["DdNA"],"%Y-%m-%d").date(), LdN=artiste_data["LdN"], adresseA=artiste_data["adresseA"], numSecuriteSociale=artiste_data["numSecuriteSociale"], numCNI=artiste_data["numCNI"], dateDelivranceCNI=datetime.strptime(artiste_data["dateDelivranceCNI"],"%Y-%m-%d").date(),dateExpirationCNI=datetime.strptime(artiste_data["dateExpirationCNI"],"%Y-%m-%d").date(),dansGroupe=artiste_data["dansGroupe"])
                db.session.add(artiste)

        if "Vehicule" in nomTable:
            vehicules = nomTable["Vehicule"]
            for vehicule_data in vehicules:
                vehicule = Vehicule(immatriculation=vehicule_data["immatriculation"], typeVehicule=vehicule_data["typeVehicule"], capacitéV=vehicule_data["capacitéV"])
                db.session.add(vehicule)

        if "Materiel" in nomTable:
            materiels = nomTable["Materiel"]

            for materiel_data in materiels:
                materiel = Materiel(materielID=materiel_data["materielID"], nomMateriel=materiel_data["nomMateriel"])
                db.session.add(materiel)

        if "Groupe" in nomTable:
            groupes = nomTable["Groupe"]
            for groupe_data in groupes:
                groupe = Groupe(groupeID=groupe_data["groupeID"], nomGroupe=groupe_data["nomGroupe"])
                db.session.add(groupe)

        if "Salle" in nomTable:
            salles = nomTable["Salle"]
            for salle_data in salles:
                salle = Salle(salleID=salle_data["salleID"], nomSalle=salle_data["nomSalle"], capaciteTotaleSalle=salle_data["capaciteTotaleSalle"], planSalle=salle_data["planSalle"], dimensionOuverture=salle_data["dimensionOuverture"], dimensionProfondeur=salle_data["dimensionProfondeur"], lieuID=salle_data["lieuID"])
                db.session.add(salle)

        if "PersonelTechnique" in nomTable:
            personels = nomTable["PersonelTechnique"]
            for personel_data in personels:
                personel = PersonelTechnique(personelTechniqueID=personel_data["personelTechniqueID"], roleID=personel_data["roleID"], nomP=personel_data["nomP"], prenomP=personel_data["prenomP"])
                db.session.add(personel)

        if "Plan" in nomTable:
            plans = nomTable["Plan"]
            for plan_data in plans:
                plan = Plan(planID=plan_data["planID"], planScene=plan_data["planScene"], planFeu=plan_data["planFeu"], salleID=plan_data["salleID"])
                db.session.add(plan)

        if "Hebergment" in nomTable:
            hebergments = nomTable["Hebergment"]
            for hebergment_data in hebergments:
                hebergment = Hebergement(hebergementID=hebergment_data["hebergementID"], nomHebergement=hebergment_data["nomHebergement"], capacitéH=hebergment_data["capacitéH"], qualitéH=hebergment_data["qualitéH"], lieuID=hebergment_data["lieuID"])
                db.session.add(hebergment)

        if "MaterielSalle" in nomTable:
            materiels = nomTable["MaterielSalle"]
            for materiel_data in materiels:
                materiel = MaterielSalle(materielSalleID=materiel_data["materielSalleID"], salleID=materiel_data["salleID"], nomMaterielS=materiel_data["nomMaterielS"], disponible=materiel_data["disponible"])
                db.session.add(materiel)

        if "Concert" in nomTable:
            concerts = nomTable["Concert"]
            for concert_data in concerts:
                concert = Concert(concertID=concert_data["concertID"], nomConcert=concert_data["nomConcert"], dateDebutConcert=datetime.strptime(concert_data["dateDebutConcert"],"%Y-%m-%d").date(), dateFinConcert=datetime.strptime(concert_data["dateFinConcert"],"%Y-%m-%d").date(), ficheTechnique=concert_data["ficheTechnique"], catering=concert_data["catering"], salleID=concert_data["salleID"], groupeID=concert_data["groupeID"])
                db.session.add(concert)

        if "MusicienAdditionnel" in nomTable:
            musiciens = nomTable["MusicienAdditionnel"]
            for musicien_data in musiciens:
                musicien = MusicienAdditionnel(musicienID=musicien_data["musicienID"], concertID=musicien_data["concertID"])
                db.session.add(musicien)

        if "Transporte" in nomTable:
            transportes = nomTable["Transporte"]
            for transport_data in transportes:
                transporte = Transporte(concertID=transport_data["concertID"], immatriculation=transport_data["immatriculation"])
                db.session.add(transporte)

        if "Necessiter" in nomTable:
            necessites = nomTable["Necessiter"]
            for necessite_data in necessites:
                necessite = Necessiter(materielID=necessite_data["materielID"], concertID=necessite_data["concertID"])
                db.session.add(necessite)

        if "Composer" in nomTable:
            compositions = nomTable["Composer"]
            for composition_data in compositions:
                composition = Composer(artisteID=composition_data["artisteID"], groupeID=composition_data["groupeID"])
                db.session.add(composition)

        if "Utilise" in nomTable:
            utilisations = nomTable["Utilise"]
            for utilisation_data in utilisations:
                utilisation = Utilise(materielArtisteID=utilisation_data["materielArtisteID"], groupeID=utilisation_data["groupeID"], quantiteMaterielArt=utilisation_data["quantiteMaterielArt"])
                db.session.add(utilisation)

        if "PARTICIPE" in nomTable:
            participations = nomTable["PARTICIPE"]
            for participation_data in participations:
                participation = Participe(concertID=participation_data["concertId"], groupeID=participation_data["groupeID"])
                db.session.add(participation)

        if "Prepare" in nomTable:
            preparations = nomTable["Prepare"]
            for preparation_data in preparations:
                preparation = Prepare(personelTechniqueID=preparation_data["personelTechniqueID"], concertID=preparation_data["concertID"])
                db.session.add(preparation)

        if "SALLETYPEPLACE" in nomTable:
            salleTypePlaces = nomTable["SALLETYPEPLACE"]
            for salleTypePlace_data in salleTypePlaces:
                salleTypePlace = SalleTypePlace(typePlaceID=salleTypePlace_data["typePlaceID"], salleID=salleTypePlace_data["salleID"], capaciteS=salleTypePlace_data["capaciteS"])
                db.session.add(salleTypePlace)

        if "ORGANISER" in nomTable:
            organisateurs = nomTable["ORGANISER"]
            for organisateur_data in organisateurs:
                organisateur = Organiser(concertID=organisateur_data["concertID"], nomOrga=organisateur_data["nomOrga"])
                db.session.add(organisateur)

    db.session.commit()




@app.cli.command()
def syncdb():
    '''Creates all missing tables.'''
    db.create_all()

@app.cli.command()
@click.argument('nomorga')
@click.argument('motDePasse')
@click.argument('typeorga')
def neworg(nomorga, motdepasse,typeorga):
    print(nomorga)
    from .models import Organisation
    from hashlib import sha256
    m = sha256()
    print(m)
    m.update(motdepasse.encode())
    print(m)
    u = Organisation(nomOrga=nomorga, motDePasse= m.hexdigest(), typeOrga=typeorga)
    db.session.add(u)
    db.session.commit()
