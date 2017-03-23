from django.shortcuts import render, reverse, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .models import Course, Dance_Style, Dance_Class, Course, Subscription, Comment
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
@login_required(redirect_field_name='dance_courses/index.html')
def showClass(request, classId):
	danceClass = Dance_Class.objects.get(id=classId)

	context = {
		'danceClass': danceClass,
		'comments': danceClass.comments.all()
	}
	return render(request, 'dance_courses/classTemplate.html', context)


##Refactor to extract show view code from subscribe unsubscribe and index

def subscribe(request, courseId):
	course = Course.objects.get(id = courseId)
	Subscription.objects.get(user=request.user).courses.add(course)
	return redirect(reverse('dance_courses:showNav'))


def unsubscribe(request, courseId):
	course = Course.objects.get(id = courseId)
	Subscription.objects.get(user=request.user).courses.remove(course)
	return redirect(reverse('dance_courses:showNav'))

def showNav(request):
	context={
		'first_name':request.user.get_short_name(),
		'subscribed_courses': Subscription.objects.get(user=request.user).courses.all(),
		'content': Dance_Style.objects.all()
	}
	return render(request, 'dance_courses/navTemplate.html', context)


def index(request):
	return render(request, 'dance_courses/index.html')

@login_required(redirect_field_name='dance_courses/index.html')
def showUserCourses(request):
	
	context={
		'first_name':request.user.get_short_name(),
		'subscribed_courses': Subscription.objects.get(user=request.user).courses.all(),
		'content': Dance_Style.objects.all()
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


def createComments(request):
	danceClass = Dance_Class.objects.get(id = request.POST['classId'])
	comment = Comment.objects.create(text=request.POST['text'],user=request.user, danceClass=danceClass)
	comment.save()
	return redirect(reverse('dance_courses:showClass', kwargs={'classId':request.POST['classId']}))

def deleteComments(request, commentId):
	comment = Comment.objects.get(id=commentId)
	comment.delete()
	classId = comment.danceClass.id
	print classId
	return redirect(reverse('dance_courses:showClass', kwargs={'classId':classId}))



	