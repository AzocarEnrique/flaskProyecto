from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class NameFormhorario(FlaskForm):
    carrera = StringField('Ingresar carrera:', validators=[DataRequired()])
    semestre = StringField('Ingresar semestre:', validators=[DataRequired()])
    buscar = SubmitField('buscar')
