from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'dance_courses/index.html')

def showUserCourses(request):
	return render(request, 'dance_courses/userCourses.html')