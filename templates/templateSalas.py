from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameFormSalas(FlaskForm):
    id = StringField('Ingresar id:')
    piso = StringField('Ingresar piso:')
    capacidad = StringField('Ingresar capacidad:')
    departamento = StringField('Ingresar Departamento:')
    ingresar = SubmitField('Ingresar')