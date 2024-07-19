from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=30,
         widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']