from app import myapp_obj, db
from flask import render_template, redirect, flash
from app.forms import LoginForm, SignUpForm, PostForm, Delete_Account_Form, SearchForm
from app.models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from datetime import datetime

@myapp_obj.route('/home')
@login_required
def homepage():
	print(current_user)
	posts = []
	for u in User.query.all():
		posts.extend(u.posts.all())
	#posts = current_user.posts.all()
	return render_template('home.html', posts=posts)
	#This will be our user home page

@myapp_obj.route('/search', methods=['POST','GET'])
@login_required
def search():
	current_form = SearchForm()
	users = User.query
	if current_form.validate_on_submit():
		user_searched = current_form.searched.data
		users = users.filter(User.username.like('%' + user_searched + '%'))
		users = users.order_by(User.username).all()
		
		return render_template("search.html", form=current_form, searched=user_searched, users = users)
	else:
		print('eugh')
		return render_template("base.html")

@myapp_obj.context_processor
def base():
	current_form = SearchForm()
	return dict(form=current_form)

@myapp_obj.route('/post', methods=['POST', 'GET'])
@login_required
def newtweet():
	current_form = PostForm()
	if current_form.validate_on_submit():
		print("post validated")
		current_datetime = datetime.now()
		post = Post(body=current_form.post.data, user_id=current_user.id, username=current_user.username, timestamp = current_datetime)
		db.session.add(post)
		db.session.commit()
		return redirect('/home')
	return render_template('post.html', form=current_form)

@myapp_obj.route('/messages', methods=['POST', 'GET'])
@login_required
def sendmsg():
	return render_template('messages.html')

@myapp_obj.route('/settings')
@login_required
def settings():
	return render_template('settings.html')

#delete account code 
@myapp_obj.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
	current_form = Delete_Account_Form()
	if current_form.validate_on_submit():

		if current_user.check_password(current_form.password.data):
			for post in current_user.posts.all():
				db.session.delete(post)
			db.session.delete(current_user)
			db.session.commit()
			print("The Account has been deleted")
			return redirect("/login")

		else:
			print("Incorrect Password!")

	return render_template('delete_account.html', form=current_form)

@myapp_obj.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

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
        return redirect('/home')
        
    return render_template('login.html', form=current_form)
#code for signup
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

@myapp_obj.route('/test', methods=['POST', 'GET'])
def test():
	return render_template('test.html')

#code for /
@myapp_obj.route('/')
def start():
	return redirect('/home')
