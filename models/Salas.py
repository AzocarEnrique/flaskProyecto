from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Salas(db.Model):
    __tablename__ = 'salas'
    id = db.Column(db.String, primary_key=True)
    piso = db.Column(db.String)
    capacidad = db.Column(db.String)
    departamento = db.Column (db.Integer, db.ForeignKey ('Departamento.numeroDpto'), nullable = False)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'piso': self.piso,
            'capacidad': self.capacidad,
            'departamento': self.departamento,
            
        }