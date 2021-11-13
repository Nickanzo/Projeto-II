from tkinter import messagebox

from BackEnd.config import *


class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(254))
    Pass = db.Column(db.String(254))

    def __str__(self):
        return str(self.id) + ") " + self.Nome + ", " + self.Pass

    def json(self):
        return {
            "id": self.id,
            "Nome": self.Nome,
            "Senha": self.Pass
        }


class Website(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(254))
    URL = db.Column(db.String(254))
    UserName = db.Column(db.String(254))
    UserPass = db.Column(db.String(254))


class Logins(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer,db.ForeignKey(Usuario.id), nullable=False)
    Website = db.Column(db.Integer,db.ForeignKey(Website.id))


def cadastraUser(name,password):
    user = Usuario(Nome=name, Pass=password)
    db.session.add(user)
    db.session.commit()


def validaUser(name):
    if not os.path.exists(arquivobd):
        messagebox.showerror("Erro", "Usuário não cadastrado")
    else:
        return db.session.query(Usuario.id).filter_by(Nome = name).first() is not None


def login(name, password):
    if not os.path.exists(arquivobd):
        messagebox.showerror("Erro","Erro na conexão com Banco!")
    else:
        return db.session.query(Usuario.id).filter_by(Nome=name,Pass=password).first() is not None


def validaBD():
    if not os.path.exists(arquivobd):
        db.create_all()


def resgataUserID(name):
    q = db.session.query(Usuario.id).filter_by(Nome=name).first()
    userID = int(q.id)
    return userID


def resgataLogins(id):
    if os.path.exists(arquivologin) and logindb.session.query(Logins.UserID).filter_by(UserID=id).first() is not None:
        return logindb.session.query(Logins.UserID).filter_by(UserID=id).count()
    else:
        return 0


if __name__ == "__main__":

    #Apaga arquivo existente
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    # Criando dados para BD
    c1 = Usuario(Nome="admin", Pass="admin")
    c2 = Usuario(Nome="user", Pass="user")

    db.session.add(c1)
    db.session.add(c2)
    db.session.commit()

    # q = db.session.query(Usuario.id).filter_by(Nome="novousuario").first()
    # userID = int(q.id)
    # print(userID)
