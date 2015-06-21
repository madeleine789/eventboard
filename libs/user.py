__author__ = 'mms'

from flask.ext.login import (UserMixin, AnonymousUserMixin)

from models import models


class User(UserMixin):
	def __init__(self, email=None, password=None, admin=False, active=True, id=None):
		self.email = email
		self.password = password
		self.active = active
		self.isAdmin = admin
		self.id = None

	def save(self):
		newUser = models.User(email=self.email, password=self.password, isAdmin=self.isAdmin, active=self.active)
		newUser.save()
		print "new user id = %s " % newUser.id
		self.id = newUser.id
		return self.id

	def get_by_email(self, email):

		dbUser = models.User.objects.get(email=email)
		if dbUser:
			self.email = dbUser.email
			self.active = dbUser.active
			self.isAdmin = dbUser.isAdmin
			self.id = dbUser.id
			return self
		else:
			return None

	def get_by_email_w_password(self, email):

		try:
			dbUser = models.User.objects.get(email=email)

			if dbUser:
				self.email = dbUser.email
				self.active = dbUser.active
				self.password = dbUser.password
				self.isAdmin = dbUser.isAdmin
				self.id = dbUser.id
				return self
			else:
				return None
		except:
			print "there was an error"
			return None

	def get_mongo_doc(self):
		if self.id:
			return models.User.objects.with_id(self.id)
		else:
			return None

	def get_by_id(self, id):
		dbUser = models.User.objects.with_id(id)
		if dbUser:
			self.email = dbUser.email
			self.active = dbUser.active
			self.isAdmin = dbUser.isAdmin
			self.id = dbUser.id

			return self
		else:
			return None

	def is_admin(self):
		return self.isAdmin


class Anonymous(AnonymousUserMixin):
	name = u"Anonymous"
