from app import myapp_obj, db
from flask import render_template, redirect, flash
from app.forms import LoginForm, SignUpForm, PostForm, Delete_Account_Form, SearchForm, FollowForm, AcceptForm
from app.models import User, Post, Follower
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
	for f in Follower.query.filter_by(user_id=current_user.id, accepted=1):
		posts.extend(User.query.filter_by(id=f.follower_id).first().posts.all())
	posts.extend(current_user.posts.all())
	posts.sort(key=Post.get_timestamp)
	posts.reverse()
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
		if current_user in users:
			users.remove(current_user)
		return render_template("search.html", form=current_form, searched=user_searched, users = users)
	return redirect('/home')

@myapp_obj.route('/follow', methods=['POST','GET'])
@login_required
def follow():
	current_form = FollowForm()
	if current_form.validate_on_submit():
		checkfollow = Follower.query.filter_by(user_id=current_form.username.data, follower_id=current_user.id).first()
		if checkfollow is not None:
			if checkfollow.accepted == 1:
				redirect('/home')
			else:
				db.session.delete(checkfollow)
				newfollow = Follower(user_id=current_user.id, follower_id=current_form.username.data, accepted=1)
				newfollow_back = Follower(user_id=current_form.username.data, follower_id=current_user.id, accepted=1)
				db.session.add(newfollow)
				db.session.add(newfollow_back)
				db.session.commit()
		else:	
			follow = Follower(user_id=current_user.id, follower_id=current_form.username.data, accepted=0)
			db.session.add(follow)
			db.session.commit()
	return redirect('/home')

@myapp_obj.context_processor
def base():
	current_form = SearchForm()
	return dict(form=current_form)

@myapp_obj.route('/post', methods=['POST', 'GET'])
@login_required
def newtweet():
	current_form = PostForm()
	if current_form.validate_on_submit():
		newimage = current_form.image.data
		if current_form.post.data is '' and newimage is '':
			return redirect('/post')
		current_datetime = datetime.now()
		post = Post(body=current_form.post.data, user_id=current_user.id, username=current_user.username, timestamp = current_datetime, image=newimage)
		db.session.add(post)
		db.session.commit()
		return redirect('/home')
	return render_template('post.html', form=current_form)

@myapp_obj.route('/messages', methods=['POST', 'GET'])
@login_required
def sendmsg():
	return render_template('messages.html')

@myapp_obj.route('/follower-requests', methods=['POST', 'GET'])
@login_required
def requests():
	current_form=AcceptForm()
	followings = Follower.query.all()
	requests = []
	for f in followings:
		if f.accepted == 0 and f.follower_id == current_user.id:
			requests.append(f)
	users = []
	for r in requests:
		users.append(User.query.filter_by(id=r.user_id).first())
	if current_form.validate_on_submit():
	
		print(User.query.filter_by(id=current_form.username.data).first())
		request = requests[users.index(User.query.filter_by(id=current_form.username.data).first())]
		db.session.delete(request)
		newfollow = Follower(user_id=current_user.id, follower_id=current_form.username.data, accepted=1)
		newfollow_back = Follower(user_id=current_form.username.data, follower_id=current_user.id, accepted=1)
		db.session.add(newfollow)
		db.session.add(newfollow_back)
		db.session.commit()
		return redirect('/home')
	return render_template('requests.html', users=users, form=current_form)

@myapp_obj.route('/settings')
@login_required
def settings():
	return render_template('settings.html')

@myapp_obj.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
	current_form = Delete_Account_Form()
	if current_form.validate_on_submit():

		if current_user.check_password(current_form.password.data):
			for post in current_user.posts.all():
				db.session.delete(post)
			for follows in Follower.query.filter_by(user_id=current_user.id):
				db.session.delete(follows)
			for follow_backs in Follower.query.filter_by(follower_id=current_user.id):
				db.session.delete(follow_backs)
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
	
    current_form = LoginForm()
    
    if current_form.validate_on_submit():
        user = User.query.filter_by(username=current_form.username.data).first()
        if user is None or not user.check_password(current_form.password.data):
            return redirect('/login')
        login_user(user)
        return redirect('/home')
        
    return render_template('login.html', form=current_form)
   
@myapp_obj.route('/signup', methods=['POST', 'GET'])
def signup():
	current_form = SignUpForm()
	if current_form.validate_on_submit():
		testuser = User.query.filter_by(username=current_form.username.data).first()
		if testuser is None:
			user = User(username=current_form.username.data, password=generate_password_hash(current_form.password.data))
			db.session.add(user)
			db.session.commit()
			login_user(user)
			return redirect('/home')
		else:
			return redirect('/signup')
	return render_template('signup.html', form=current_form)


@myapp_obj.route('/')
def start():
	db.create_all()
	return redirect('/home')
