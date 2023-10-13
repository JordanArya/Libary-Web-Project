from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from datetime import timedelta
from os import path



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data/data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"

bcrypt = Bcrypt(app)

def create_app():
	app.config['SECRET_KEY'] = 'adwad$aidwaik***dadwaddmawdkwa'

	from .views import views
	from .auth import auth

	app.register_blueprint(views,url_prefix='/')
	app.register_blueprint(auth,url_prefix='/')

	create_database(app)

	return app

def create_database(app):
	if not path.exists('website/data/data.db'):
		db.create_all(app=app)
		print('Created Database!')
