from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameFormMostrar(FlaskForm):
    id = StringField('Ingresar id:', validators=[DataRequired()])
    ingresar = SubmitField('Ingresar')
