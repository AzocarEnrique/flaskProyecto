from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameFormLogin(FlaskForm):
    operador= SelectField("Cargo", choices=[("Administrador","Administrador"),("Profesor","Profesor")])
    rut = StringField('Ingresar rut:')
    contrasena = StringField('Ingresar Contraseña:')
    ingresar = SubmitField('Ingresar')
    