from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from api.models import Category


class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]


