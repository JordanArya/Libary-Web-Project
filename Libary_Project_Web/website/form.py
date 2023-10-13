from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError,DateField,IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo,NumberRange
from datetime import date
import datetime 




class RegistarationForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	password = PasswordField('Password',validators=[DataRequired(),Length(min=8),EqualTo('confirm_password',message='Your Confirm Password Not Match')])
	confirm_password = PasswordField('Confirm Password',validators=[DataRequired()])
	submit = SubmitField('SignUp')

class LoginForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	password =  PasswordField('Password',validators=[DataRequired()])
	submit = SubmitField('Login')

class AddBook(FlaskForm):
	title = StringField('Title', validators=[DataRequired()]) 
	volume = IntegerField('Volume', validators=[DataRequired()])
	author = StringField('Author', validators=[DataRequired()])
	release_date = DateField(validators=[DataRequired()], default= date.today)
	placement = StringField('Placement', validators=[DataRequired()]) 
	image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
	submit = SubmitField('Submit')







