from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8)])
    submit = SubmitField('Sign Up')

class PostForm(FlaskForm):
	post = TextAreaField('Post', validators=[Length(max=140)])
	image = StringField('Image')
	submit = SubmitField('Post')

class Delete_Account_Form(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Delete Account')

class SearchForm(FlaskForm):
	searched = StringField('Searched', validators=[DataRequired()])
	submit = SubmitField('Search')

class FollowForm(FlaskForm):
	username = HiddenField('User')
	submit = SubmitField('Follow')

class AcceptForm(FlaskForm):
	username = HiddenField('username')
	submit = SubmitField('Accept')
