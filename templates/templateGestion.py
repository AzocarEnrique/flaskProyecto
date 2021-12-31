from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class NameFormGestion(FlaskForm):
    operador= SelectField("Cargo", choices=[("Agregar","Agregar Salas"),("Cuentas","Administrar cuentas"),
    ("Peticion","Autorizar peticiones de salas"), ("Horario","Subir Horario")])
    ingresar = SubmitField('Ingresar')