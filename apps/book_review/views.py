from django.shortcuts import render, redirect, reverse
from .models import Review, Book
from ..login_reg_app.models import User

# Create your views here.
def index(request):

	context={
		'user':User.objects.get(id=request.session['userId']),
		'reviews':Review.objects.order_by('-created_at')[:4]
	}

	return render(request, 'book_review/index.html', context)

def logout(request):
	return redirect(reverse('book_review:index'))

def new(request):
	return render(request, 'book_review/addBookAndReview.html')

def add(request):
	book = Review.objects.new(request.POST, request.session['userId'])
	return redirect(reverse('book_review:show', kwargs={'book_id':book.id}))

def destroy(request, review_id):
	response = Review.objects.destroy(review_id)
	return redirect(reverse('book_review:index'))

def show(request, book_id):
	
	book = Book.objects.get(id=book_id)

	context={
		'book':book,
		'reviews':book.reviews.all()
	}
	return render(request, 'book_review/book.html', context)

	

