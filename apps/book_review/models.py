from __future__ import unicode_literals
from ..login_reg_app.models import User
from django.db import models

# Create your models here.

class ReviewManager(models.Manager):

	def new(self, postData, user_id):
		user = User.objects.get(id=user_id)

		if 'book_id' in postData:
			book = Book.objects.get(id=postData['book_id'])
		else:
			if postData['new_author']=='':
				author = postData['author']
			else:
				author=postData['new_author']

			book = Book.objects.create(title=postData['title'], author=author)
			book.save()

		newReview = Review.objects.create(rating=postData['rating'], review=postData['review'], reviewer =user, book=book)
		newReview.save()
		return book

	def destroy(self, review_id):
		review = Review.objects.get(id=review_id)
		review.delete()
		return 'success'


class Book(models.Model):
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=50)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

class Review(models.Model):
	rating = models.IntegerField()
	review=models.CharField(max_length = 1000)
	reviewer=models.ForeignKey(User,related_name='reviews')
	book = models.ForeignKey(Book, related_name='reviews')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	objects=ReviewManager()




		