from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(200))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    following = db.relationship('Follower', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	username = db.Column(db.String)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, default=datetime)
	image = db.Column(db.String)
	reposted_from = db.Column(db.String())
	likes = db.relationship('Like', backref='post', lazy='dynamic')

	def get_timestamp(self):
		return self.timestamp

class Follower(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	follower_id = db.Column(db.Integer)
	accepted = db.Column(db.Integer)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	sender_username = db.Column(db.String)
	body = db.Column(db.String(240))

class Like(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('post.id'))	
	post_id = db.Column(db.Integer)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
