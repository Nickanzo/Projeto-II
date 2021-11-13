#imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

### Criação BD de Usuários ###
app = Flask(__name__)

#Caminho Arquivo BD
path = os.path.dirname(os.path.abspath(__file__))
#Nome de Arquivo
arquivobd = os.path.join(path, 'user.db')

#SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
#Ignora Avisos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


### Criação BD Logins ###
logapp = Flask(__name__)

arquivologin = os.path.join(path, 'login.db')

#SQLAlchemy
logapp.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivologin
#Ignora Avisos
logapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

logindb= SQLAlchemy(logapp)


### Criação BD Websites ###
websites = Flask(__name__)

arquivowebsites = os.path.join(path, 'websites.db')

#SQLAlchemy
websites.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivowebsites
#Ignora Avisos
websites.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

websites = SQLAlchemy(logapp)
