from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def register(self,postData):
		
		response = {'passed':True, 'error_fields':[]}
		first_name = postData['first_name']
		last_name = postData['last_name']
		email=postData['email']
		password=postData['password'].encode('utf-8')
		confirm_pw=postData['confirm_pw']

		#Validations
		if len(first_name)<2 or (not first_name.isalpha()):
			response['passed']=False
			response['error_fields'].append("first_name")

		if len(last_name)<2 or (not last_name.isalpha()):
			response['passed']=False
			response['error_fields'].append("last_name")

		if len(email)<1 or (not EMAIL_REGEX.match(email)):
			response['passed']=False
			response['error_fields'].append("email")
			
		if len(password)<8 or password != confirm_pw:
			response['passed']=False
			response['error_fields'].append("password")
		
		#Add User if Validations Pass		
		if response['passed']:
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())
			user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
			response['userId'] = user.id
		
		return response


	def login(self,postData):

		email=postData['email']
		password=postData['password'].encode('utf-8')

		if User.objects.filter(email=email).exists():

			user = User.objects.filter(email=email).values()
			hashed = user[0]['password'].encode('utf-8')

			if bcrypt.hashpw(password,hashed)==hashed:

				userId = user[0]['id']
				return {'passed':True, 'userId':userId}

		return {'passed':False}



class User(models.Model):
	first_name=models.CharField(max_length=55)
	last_name=models.CharField(max_length=55)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects=UserManager()



