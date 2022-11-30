from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    newUsername = StringField('Username', validators=[DataRequired()])
    newPassword = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
