from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
def index(request):
	return render(request, 'dance_courses/index.html')

@login_required(redirect_field_name='dance_courses/index.html')
def showUserCourses(request):
	context={
		'first_name':request.user.get_short_name()
	}
	return render(request, 'dance_courses/userCourses.html', context)

def createUsers(request):

	if User.objects.filter(username=request.POST['username']).exists():
		return HttpResponse("Existing account with this email", status=403)
	else:
		user = User.objects.create_user(first_name=request.POST['firstname'], last_name=request.POST['lastname'], username = request.POST['username'], email=request.POST['username'], password=request.POST['password'])
	
		if user is not None:
			user.save()
			print 'user  saved'
			user = authenticate(username=request.POST['username'], password=request.POST['password'])
			login(request,user)
			return redirect(reverse('dance_courses:showUserCourses'))
		else:
			return HttpResponse("Had an unknown issue registering, sorry! Please reach out to our people.", status=403)

def loginUsers(request):
	response_data = {}

	user = authenticate(username=request.POST['username'], password=request.POST['password'])

	if user is not None:
		login(request,user)
		return redirect(reverse('dance_courses:showUserCourses'))

	else:
		return HttpResponse("Invalid username/password combination", status=403)


def logoutUsers(request):
	logout(request)
	return redirect(reverse('dance_courses:index'))

	