from .models import Room
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms

class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=['host','participants']
        
# class UserForm(ModelForm):
#     class Meta:
#         model=User
#         fields=["username","email"]        
#         from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = ("username", "email",  "password1", "password2")