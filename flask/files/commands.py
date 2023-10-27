import click
from .app import app,db

@app.cli.command()
@click.argument('filename')

def loaddb(filename):
    '''Creates the tables and populates them with data'''
    #créationdetouteslestables
    db.create_all()
    #chargementdenotrejeudedonnées
    import yaml
    file = yaml.safe_load(open(filename))
    #importdesmodèles
    from .models import Organisation
    #premièrepasse:créationdetouslesauteurs
    organisations={}
    for o in file:
        nom=o["nomOrga"]
        mdp = o["motDePasse"]
        type = o["typeOrga"]
        if nom not in organisations:
            org = Organisation(nomOrga=nom, motDePasse=mdp, typeOrga=type)
            db.session.add(org)
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