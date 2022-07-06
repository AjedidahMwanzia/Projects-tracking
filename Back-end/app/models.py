
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils  import timezone
from cloudinary.models import CloudinaryField


class Cohort(models.Model):
    name = models.CharField(max_length=100)
    admission_date = models.DateTimeField(auto_now_add=True,blank=True)
    graduation_date = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return str(self.name)

    def save_cohort(self):
        self.save()

class User(AbstractUser):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    username= models.CharField(max_length=255,unique=True)
    cohort=models.OneToOneField(Cohort,on_delete=models.SET_NULL,null=True)
    # project=models.ForeignKey(Project,on_delete=CASCADE)
    # USERNAME_FIELD='email'
    # REQUIRED_FIELDS=[]




class Project(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    project_image = CloudinaryField('image')
    url = models.URLField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

    def save_projects(self):
        self.user

    def delete_projects(self):
        self.delete()    

    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=300)
    image = CloudinaryField('image')
    phone_number = models.TextField(max_length=12)
    facebookLinks = models.CharField(max_length=1000, null=True)
    TwitterLinks = models.CharField(max_length=10000, null=True)
    GithubLinks = models.CharField(max_length=1000, null=True)
    InstagramLinks = models.CharField(max_length=1000, null=True)
     

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


