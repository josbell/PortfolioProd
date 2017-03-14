from django.shortcuts import render, redirect, reverse

# Create your views here.
def home(request):
	return render(request, 'portfolio/index.html')