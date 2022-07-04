from django.urls import path
from . import  views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('api/projects',views.ProjectList.as_view(), name='apiprojects')
]