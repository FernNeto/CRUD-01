from database import db

class Usuario(db.Model):
  __tablename__="usuario"  
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  email = db.Column(db.String(100))
  senha = db.Column(db.String(100))
  tipo = db.Column(db.String(15))

  def __init__(self, nome, email, senha, tipo):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.tipo = tipo

  def __repr__(self):
    return "Usuario: {}".format(self.nome)
    
