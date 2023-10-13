from website import db, login_manager

from flask_login import UserMixin

from datetime import datetime

#This function for UserMixin in flask_login
@login_manager.user_loader
def load_user(id):
	return User.query.get(id)

#FLASK ORM - SQLAlchemy Object Relation Model (ORM)
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, db.Identity(start = 1, cycle=True) ,primary_key = True)
	username = db.Column(db.String(20),unique = True, nullable = False)
	password = db.Column(db.String(20), nullable = False, unique = True)
	books =  db.relationship('Books', backref = "creator", lazy = True)
 	

class Books(db.Model):
	id = db.Column(db.Integer, db.Identity(start = 1, cycle = True), primary_key = True)
	upload_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	title = db.Column(db.String(20), nullable = False) 
	volume = db.Column(db.String(20), nullable = False)
	author = db.Column(db.String(20), nullable = False)
	placement = db.Column(db.String(20), nullable = False) 
	release_date = db.Column(db.String(20), nullable=False)
	image_file = db.Column(db.String(100), unique = True, nullable = False)
	creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	book_id = db.Column(db.Integer, nullable = False)




