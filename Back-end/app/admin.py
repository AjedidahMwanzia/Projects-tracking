from django.contrib import admin
from .models import Cohort ,Project,User,Profile

# Register your models here.
admin.site.register(Cohort)
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(User)
