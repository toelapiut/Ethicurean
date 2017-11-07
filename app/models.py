from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
class User(UserMixin,db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(255),unique=True,index=True)
	email=db.Column(db.String(255),unique=True,index=True)
	bio=db.Column(db.String(255))
	password_hash = db.Column(db.String(255))
	admin = db.Column(db.Boolean, nullable=False, default=False)
	confirmed_on = db.Column(db.DateTime, nullable=True)
	comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
	blogs=db.relationship('Blog',backref='user',lazy='dynamic')

		

	@property
	def password(self):
		raise AttributeError('You cannnot read the password attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)


	def verify_password(self,password):
		return check_password_hash(self.password_hash,password)

	def __repr__(self):
		return f'User {self.username}'


class Blog(db.Model):
	__tablename__='blogs'
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(100))
	blog=db.Column(db.String(1000))
	user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
	comments=db.relationship('Comment',backref='blog',lazy='dynamic')

	def save_blog(self):
		db.session.add(self)
		db.session.commit()

class Comment(db.Model):
	__tablename__='comments'
	id=db.Column(db.Integer,primary_key=True)
	review=db.Column(db.String(255))
	blog_id=db.Column(db.Integer,db.ForeignKey("blogs.id"))
	user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
	

