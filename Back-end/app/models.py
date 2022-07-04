from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils  import timezone
from cloudinary import CloudinaryImage


class Project(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    project_image = CloudinaryImage('image')
    project_link = models.URLField(max_length=20000)
    date_posted = models.DateTimeField(default=timezone.now)

    def save_projects(self):
        self.user

    def delete_projects(self):
        self.delete()    

    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=300)
    image = CloudinaryImage('image')
    email = models.EmailField()
    phone_number = models.TextField(max_length=12)
    facebookLinks = models.CharField(max_length=1000, null=True)
    TwitterLinks = models.CharField(max_length=10000, null=True)
    GithubLinks = models.CharField(max_length=1000, null=True)
    InstagramLinks = models.CharField(max_length=1000, null=True)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='profile')

class Cohort(models.Model):
    name = models.CharField(max_length=100)
    admission_date = models.DateTimeField(auto_now_add=True,blank=True)
    graduation_date = models.DateTimeField(auto_now_add=True,blank=True)