from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
	if 'userId' in request.session:
		return redirect(reverse('book_review:index'))
	else:
		return render(request, 'login_reg_app/index.html')

def addUser(request):
	validation_response = User.objects.register(request.POST)

	if validation_response['passed']:
		messages.add_message(request, messages.SUCCESS, 'Successfully registered')
		request.session['userId']=validation_response['userId']
		return redirect(reverse('book_review:index'))
	else:
		for error_field in validation_response['error_fields']: 
			messages.add_message(request, messages.INFO, error_field)

		return redirect(reverse('login_reg:index'))

def login(request):
	validation_response = User.objects.login(request.POST)

	if validation_response['passed']:
		messages.add_message(request, messages.SUCCESS, 'Successfully logged in')
		request.session['userId']=validation_response['userId']
		return redirect(reverse('book_review:index'))
	else:
		messages.add_message(request, messages.INFO, 'login_failed')
		return redirect(reverse('login_reg:index'))


