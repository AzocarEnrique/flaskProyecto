from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Ingresar nombre:', validators=[DataRequired()])
    age = StringField('Ingresar edad:')
    address = StringField('Ingresar direccion:')
    submit = SubmitField('Submit')
