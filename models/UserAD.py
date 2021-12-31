from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    __tablename__ = 'administrador'
    rut = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    email = db.Column(db.String(120))
    contrasena = db.Column(db.String)
    departamento = db.Column(db.String)
    oficina = db.Column(db.String)
    cargo = db.Column(db.String)

    @property
    def serialize(self):
        return{
            'rut': self.rut,
            'nombre': self.nombre,
            'email': self.email,
            'contrasena': self.contrasena,
            'departamento': self.departamento,
            'oficina': self.oficina,
            'cargo': self.cargo
        }
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
class Salas(db.Model):
    __tablename__ = 'salas'
    id = db.Column(db.String, primary_key=True)
    piso = db.Column(db.String)
    capacidad = db.Column(db.String)
    departamento = db.Column (db.String)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'piso': self.piso,
            'capacidad': self.capacidad,
            'departamento': self.departamento,
            
        }

class Horario(db.Model):
    __tablename__ = 'horario'
    carrera = db.Column(db.String, primary_key=True)
    semestre = db.Column(db.String)
    imagen = db.Column(db.String(), nullable=True)

    @property
    def serialize(self):
        return{
            'carrera': self.carrera,
            'semestre': self.semestre,
            'imagen': self.imagen  
        }