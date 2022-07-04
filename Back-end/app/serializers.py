from rest_framework import serializers
from .models import Profile,Project, Cohort
from django.contrib.auth.models import User



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('__all__')
        
class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('name', 'description', 'project_image','project_link','user') 

class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort 
        fields = ('name', 'admission_date', 'graduation_date')
