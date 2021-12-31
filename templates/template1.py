from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class NameFormop(FlaskForm):
    operador= SelectField("Cargo", choices=[("Administrador","Administrador"),("Profesor","Profesor")])
    ingresar = SubmitField('Ingresar')