from app import myapp_obj, db
from flask import render_template, redirect, flash
from app.forms import LoginForm, SignUpForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

@myapp_obj.route('/home')
@login_required
def home():
	return render_template('base.html')
	#This will be our user home page

@myapp_obj.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():

	#Login will need to have link to sign-up page
	
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        # search to make sure we have the user in our database
        user = User.query.filter_by(username=current_form.username.data).first()

        # check user's password with what is saved on the database
        if user is None or not user.check_password(current_form.password.data):
            flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect('/login')

        # login user
        login_user(user)
        return redirect('/')
        
    return render_template('login.html', form=current_form)

@myapp_obj.route('/signup', methods=['POST', 'GET'])
def signup():
	current_form = SignUpForm()
	if current_form.validate_on_submit():
		user = User(username=current_form.username.data, password=generate_password_hash(current_form.password.data))
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect('/home')
	return render_template('signup.html', form=current_form)

@myapp_obj.route('/')
def start():
	# Make this page redirect to login if not signed in, or homepage if signed in
	# already done by making the home redirect to login when not signed in :)
    return redirect('/home')
