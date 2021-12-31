from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class NameFormautorizo(FlaskForm):
    rut = StringField('Ingresar rut:', validators=[DataRequired()])
    ingresar = SubmitField('Eliminar')