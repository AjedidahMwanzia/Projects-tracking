from wsgiref import validate
from rest_framework import serializers
from .models import Profile,Project, Cohort, User



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ('name', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
        
class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('name', 'description', 'project_image','project_link','user') 

class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort 
        fields = ('name', 'admission_date', 'graduation_date')
