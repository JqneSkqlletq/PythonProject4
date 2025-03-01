from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, ValidationError, length
from wtforms import SubmitField,  StringField, PasswordField, BooleanField

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(), length(min=2)])
    pasword = PasswordField('Password',validators=[DataRequired(), length(min=3, max=6)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

