from django import forms
from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=120)
    email = forms.EmailField()
    password = forms.CharField(max_length=255)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=255)
