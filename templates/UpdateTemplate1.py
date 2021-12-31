from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameForm1(FlaskForm):
    rut = StringField('Ingresar rut:')
    nombre = StringField('Ingresar nombre:')
    email = StringField('Ingresar email:')
    contrasena = StringField('Ingresar contraseña:')
    departamento = StringField('Ingresar Departamento:')
    ingresar = SubmitField('Ingresar')