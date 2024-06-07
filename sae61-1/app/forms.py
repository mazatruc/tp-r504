from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=10), 
                                                   Regexp('^[a-z0-9]+$', message='Username must have only lowercase alphanumeric characters.')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=15), 
                                                     Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[A-Za-z\d@#$%^&+=]{6,15}$', 
                                                            message='Password must have at least 6 characters, with one uppercase letter, one lowercase letter, one digit, and one of #@%{} characters.')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')
