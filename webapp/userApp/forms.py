from django import forms
#using User model from django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Item

# User registration form

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('itemName','itemURL','itemPrice')

