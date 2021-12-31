from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Profesor(db.Model):
    __tablename__ = 'profesores'
    rut = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    email = db.Column(db.String(120))
    contrasena = db.Column(db.String)
    departamento = db.Column(db.String)
    #departamento = db.Column (db.Integer, db.ForeignKey ('Departamento.numeroDpto'), nullable = False)

    @property
    def serialize(self):
        return{
            'rut': self.rut,
            'nombre': self.nombre,
            'email': self.email,
            'contrasena': self.contrasena,
            'departamento': self.departamento
        }