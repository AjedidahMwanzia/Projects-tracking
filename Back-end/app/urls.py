
from django.urls import path
from . import  views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    
    path('',views.home,name='home'),
    # path('register/',views.RegisterView.as_view(),name = 'register'),
    # path('login/',views.LoginView.as_view(),name = 'login'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('api/user', views.UserView.as_view(), name='user'),
    path( 'logout', views.LogoutView.as_view(), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='auth/login.html'), name='logout'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/users/', views.UserList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('api/projects',views.ProjectList.as_view()),
    path('api/cohort/', views.CohortList.as_view()),
    # path('auth/login/', obtain_auth_token),
    # path('auth/refresh-token/', refresh_auth_token),

]