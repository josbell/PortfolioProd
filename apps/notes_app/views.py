from django.shortcuts import render, reverse, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Note

# Create your views here.
def loginUsers(request):
	if request.method =='POST':
		print request.POST['username']
		print request.POST['password']
		user = authenticate(username=request.POST['username'], password =request.POST['password'])
		if user is not None:
			login(request,user)
			return redirect(reverse('notes_app:userNotes'))
		else:
			return HttpResponse('invalid login')
	else:
		form = AuthenticationForm(request.POST)
		context = {
			'form': form
		}
		return render(request, 'notes_app/login.html', context)

def registerUsers(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect(reverse('notes_app:userNotes'))
		else:
			return HttpResponse('failed to register')
	else:
		form = UserCreationForm()
		context = {
			'form': form
		}
		return render(request, 'notes_app/register.html', context)

@login_required(login_url='/')
def userNotes(request):
	context = {
		'notes':Note.objects.order_by('-created_at').all()
	}
	return render(request, 'notes_app/notesHome.html', context)

def showNotesOnly(request):
	context = {
		'notes':Note.objects.order_by('-created_at').all()
	}
	return render(request, 'notes_app/notes.html', context)

def newNote(request):
	note = Note.objects.new(request.POST, request.user)
	if note is not None:
		return redirect(reverse('notes_app:showNotesOnly'))
	else:
		return HttpResponse('failed saving note')

def destroy(request, id):
	deleted = Note.objects.destroy(id)
	if deleted:
		return redirect(reverse('notes_app:userNotes')) 
	else:
		return HttpResponse('failed deleting note')



