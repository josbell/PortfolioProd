from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class NoteManager(models.Manager):
	def new(self, postData, user):
		note = Note.objects.create(title=postData['title'], text=postData['text'], user=user)
		note.save()
		return note

	def destroy(self, note_id):
		note = Note.objects.get(id=note_id)
		note.delete()
		return True


# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length=50)
	text = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user = models.ForeignKey(User, related_name = 'notes')
	objects = NoteManager()

	def __str__(self):
		return self.text		