__author__ = 'mms'

from models import models
from flask.ext.mongoengine.wtf import model_form
from wtforms.fields.html5 import DateTimeField
from wtforms.fields import TextField, PasswordField, StringField
from flask.ext.mongoengine.wtf.orm import validators
from libs.datetime import DateTimePickerWidget


user_form = model_form(models.User, exclude=['password'])
event_form = model_form(models.Event, exclude=['comments', 'user', 'last_updated'])

class SignupForm(user_form):
	password = PasswordField('Password', validators=[validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
	confirm = PasswordField('Repeat Password')


class LoginForm(user_form):
	password = PasswordField('Password', validators=[validators.DataRequired()])

'''
class EventForm(event_form):
	title = StringField(validators=[validators.DataRequired()])
	description = StringField(validators=[validators.DataRequired()])
	starting_at = DateTimeField('StartDatePicker', validators=[validators.DataRequired()], widget=DateTimePickerWidget())
	ending_at = DateTimeField('EndDatePicker', validators=[validators.DataRequired()], widget=DateTimePickerWidget())
'''


