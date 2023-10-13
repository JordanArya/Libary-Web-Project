# Flask Things
from flask import Blueprint,render_template,request,redirect,url_for,flash,session,jsonify
from flask_login import login_required,current_user


from website import app, db
from website.model import User,Books

from .form import AddBook

# Anything else
import base64
import json
from PIL import Image
from werkzeug.utils import secure_filename
import os
import time
import secrets
import datetime

views = Blueprint('views',__name__)






# Route

	# Home index

@views.route("/home", methods = ["GET", "POST"])
@views.route("/", methods = ["GET", "POST"])
@login_required
def home():
	form = AddBook()
	if upload_image(form):
		return redirect(url_for('views.home'))

	current_user.books.reverse()

	return render_template('home.html',form=form, user=current_user, book_list = current_user.books)

# Libary index
@views.route("/libary", defaults={'edit': None}, methods = ["GET", "POST"])
@views.route("/libary/<edit>", methods = ["GET", "POST"])
@login_required
def libary(edit):
	form = AddBook()
	if upload_image(form):
		return redirect(url_for('views.libary'))

	current_user.books.reverse()
	return render_template('libary.html',form=form, user=current_user, book_list = current_user.books, edit = edit)

# Content index
@views.route("/content", defaults={'id':0}, methods = ["GET", "POST"])
@views.route("/content/<id>", methods = ["GET", "POST"])
@login_required
def content(id,edit=None):
	form = AddBook()
	if request.args.get('edit') == "True":
		if update_image(form, id):
			return redirect(url_for('views.content'))

	else:
		if upload_image(form):
			return redirect(url_for('views.content'))

	book = current_user.books[int(id)]

	return render_template('content.html',form=form, user=current_user, book_data=book, edit = edit)


@views.route("/content/<id>/delete")
@login_required
def delete(id):
	book = Books.query.get_or_404(id)

	if book:


		db.session.delete(book)
		db.session.commit()

		book_path = os.path.join(app.root_path, 'static', book.image_file)

		if os.path.exists(book_path):
			os.remove(book_path)
		else:
			raise ValueError("data not found")
		


	return redirect(url_for("views.libary"))


# DataBase Settings

	# Random picture file name

def update_image(form,id):
	if form.validate_on_submit():
		title = form.title.data
		volume = str(form.volume.data) 
		author = form.author.data 
		release_date = form.release_date.data
		placement = form.placement.data
		imagefile = form.image.data
		print(id)
		book = Books.query.filter_by(id=id).first()
		
		

def upload_image(form):
	if form.validate_on_submit():
		title = form.title.data
		volume = str(form.volume.data) 
		author = form.author.data 
		release_date = form.release_date.data
		placement = form.placement.data
		imagefile = form.image.data

		user_path = made_path()
		image_name = random_data(imagefile)
		image_file = save_image(imagefile, user_path, image_name)

		book_id = ( int(len(current_user.books)) + 1)

		book = Books(book_id = book_id, title = title, volume = volume, author = author, release_date = release_date, placement = placement, image_file = image_file, creator_id = current_user.id)
		db.session.add(book)
		db.session.commit()

		return True
	else:
		return False
		

def made_path():
	path = os.path.join(app.root_path, 'static/Book_Picture', current_user.username)
	if not os.path.exists(path):
		os.makedirs(path)

	return path


def random_data(form_picture):
	random_file_name = secrets.token_hex(16)
	f_name, f_ext = os.path.splitext(form_picture.filename)
	picture_file_name = random_file_name + f_ext

	return picture_file_name

#SAVE IMAGE
def save_image(input_image, paths, name):

	output_size = (540,450)
	path = os.path.join(paths, name)
	image = Image.open(input_image)
	image.thumbnail(output_size)
	image.save(path)
	filename = (os.path.join('Book_Picture', current_user.username, name)).replace("\\","/")

	return filename






