
from django.urls import path
from . import  views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    
    path('',views.home,name='home'),
    path('register/',views.register_user,name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/login.html'), name='logout'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/user/', views.UserList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('api/projects',views.ProjectList.as_view()),
    path('api/cohort/', views.CohortList.as_view()),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh-token/', refresh_jwt_token),

]