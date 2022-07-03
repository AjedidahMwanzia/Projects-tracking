from os import pathsep
from django.urls import path
from . import  views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('',views.home,name='home'),
    path('register/',views.register_user,name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/login.html'), name='logout'),
    path('api/profile/', views.ProfileList.as_view())
]