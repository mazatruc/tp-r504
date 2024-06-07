from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp

class RegistrationForm(FlaskForm):
    username = StringField('Identifiant', validators=[DataRequired(), Length(min=6, max=10), Regexp('^[a-z]*$')])
    password = PasswordField('Mot de passe', validators=[
        DataRequired(),
        Length(min=6, max=15),
        Regexp('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[#%{}@]).{6,15}$')
    ])
    email = StringField('Adresse e-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Valider')
