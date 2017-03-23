from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Dance_Style(models.Model):
	name = models.CharField(max_length=30)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	
	def __str__(self):
			return self.name

class Course(models.Model):
	dance_style = models.ForeignKey(Dance_Style,on_delete=models.CASCADE, related_name='courses')
	name = models.CharField(max_length=30)
	short_name = models.CharField(max_length=30)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Dance_Class(models.Model):
	name = models.CharField(max_length=30)
	order = models.IntegerField(null=True)
	url = models.CharField(max_length=200, null=True)
	course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='videos')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Subscription(models.Model):
	name = models.CharField(max_length=30)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscriptions', primary_key=True)
	courses = models.ManyToManyField(Course)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)


class Comment(models.Model):
	text = models.CharField(max_length=200)
	user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='comments')
	danceClass = models.ForeignKey(Dance_Class, on_delete=models.CASCADE, related_name = 'comments')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)






