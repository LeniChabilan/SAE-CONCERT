from flask import Flask
from flask_bootstrap import Bootstrap5
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_dropzone import Dropzone

app = Flask(__name__)
login_manager = LoginManager(app)
app.config['UPLOADED_TEMP_DEST'] = os.path.normpath(os.path.join(os.path.dirname(__file__), 'static/temp'))
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_DEFAULT_MESSAGE'] = 'Glissez vos fichiers PDF'
app.config['DROPZONE_MAX_FILE_SIZE'] = 2048
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '.pdf'
bootstrap = Bootstrap5(app)
dropzone = Dropzone(app)

def mkpath(p):
    return os.path. normpath (
        os.path.join(
            os.path.dirname(__file__),
            p))

#app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../../creaConcert.db'))
login='chabilan'
passwd='chabilan'
serveur='servinfo-maria'
bd='DBchabilan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://'+login+':'+passwd+'@'+serveur+'/'+bd
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "4d166f5f-fa64-461b-878d-d7077d4ef1a2"

login_manager.login_view = "connexion"