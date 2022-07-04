from django import forms
from .models import Project

class projectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','project_image','project_link']