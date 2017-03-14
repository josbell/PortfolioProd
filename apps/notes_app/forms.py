from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	username = forms.CharField(max_length=45)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
	first_name = forms.CharField(max_length=45)
	last_name = forms.CharField(max_length=45)
	username = forms.CharField(max_length=45)
	email = forms.EmailField()
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)
	confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)
