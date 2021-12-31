from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Horario(db.Model):
    __tablename__ = 'horario'
    hora_ini = db.Column(db.String, primary_key=True)
    hora_fin = db.Column(db.String)
    dia = db.Column(db.String)
    idSala = db.Column (db.Integer, db.ForeignKey ('Salas.id'), nullable = False)
    rutProfesor = db.Column (db.Integer, db.ForeignKey ('UserP.rut'), nullable = False)
    asignatura = db.Column(db.String)
    carrera = db.Column(db.String)

    @property
    def serialize(self):
        return{
            'hora_ini': self.hora,
            'hora_fin': self.hora,
            'dia': self.dia,
            'idSala': self.idSala,
            'rutProfesor': self.rutProfesor,
            'asignatura': self.asignatura,
            'carrera': self.carrera,
        }