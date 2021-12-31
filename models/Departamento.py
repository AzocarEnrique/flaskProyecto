from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Departamento(db.Model):
    __tablename__ = 'departamento'
    numeroDpto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    @property
    def serialize(self):
        return{
            'numeroDpto': self.numeroDpto,
            'nombre': self.nombre,
            
        }