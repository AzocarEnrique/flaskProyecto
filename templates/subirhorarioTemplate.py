from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class NameFormsubirhorario(FlaskForm):
    carrera = StringField('Ingresar carrera:', validators=[DataRequired()])
    semestre = StringField('Ingresar semestre:', validators=[DataRequired()])
    imagen = FileField("Horario")
    ingresar = SubmitField('Ingresar')
