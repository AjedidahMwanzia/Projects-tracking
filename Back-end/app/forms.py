
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Project


class UserRegistrationForm(UserCreationForm):
   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class projectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','project_image','url']

