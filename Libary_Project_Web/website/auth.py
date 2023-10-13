from flask import Blueprint,render_template,redirect,request,flash,url_for
from flask_login import login_user, current_user, logout_user, login_required

# Import dari file lain
from website import app, db, bcrypt
from .form import RegistarationForm,LoginForm
from .model import User

# Import lain
from datetime import timedelta

auth = Blueprint('auth',__name__)

@auth.route("/login", methods = ['GET','POST'])
def login():
	form = LoginForm()
	if current_user.is_authenticated:
		return redirect(url_for("views.home"))
	if form.validate_on_submit():
		username = form.username.data 
		password = form.password.data
		username = username.lower()
		authentication_user = User.query.filter_by(username=username).first()
		if authentication_user:
			if bcrypt.check_password_hash(authentication_user.password,password):
				flash('Logged in succesfully!',category='success')
				login_user(authentication_user ,duration = timedelta(seconds=1))
				return redirect(url_for('views.home'))
			else:
				flash('Incorrect password, try again.',category='error')
		else:
			flash("Username does not exist.",category='error')

	return render_template('login.html',form = form, user=current_user)

@auth.route("/signup", methods = ['GET','POST'])
def signup():
	form = RegistarationForm()
	if current_user.is_authenticated:
		return redirect(url_for("views.home"))

	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		username = username.lower()
		authentication_user = User.query.filter_by(username=username).first()
		if username != "null" or username != None:
			if authentication_user is None:	
				new_user = User(username = username,password=bcrypt.generate_password_hash(password))
				db.session.add(new_user)
				db.session.commit()

				login_user(new_user,duration = timedelta(seconds=1))
				
				return redirect(url_for('views.home'))
			else:
				flash('username already exist',category='error')

	return render_template('signup.html',form = form, user=current_user)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('views.home'))