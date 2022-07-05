
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api


from rest_framework.response import Response
from rest_framework.views import APIView

from app.permissions import IsAdminOrReadOnly
from .models import  Profile,Project,Cohort
from .serializers import ProfileSerializer, UserSerializer,ProjectSerializer, CohortSerializer
from django.contrib.auth.models import User
from rest_framework import status


# Create your views here.
def home(request):
    return render(request,'index.html')


class ProjectList(APIView):
    def get(self,request,format = None):
        all_projects = Project.objects.all()
        serializerdata = ProjectSerializer(all_projects,many = True)
        return Response(serializerdata.data)

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'auth/register.html', context)


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_user = User.objects.all()
        serializers = UserSerializer(all_user, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CohortList(APIView):
    def get(self, request, format=None):
        all_cohorts = Cohort.objects.all()
        serializers = CohortSerializer(all_cohorts, many=True)
        permission_classes = (IsAdminOrReadOnly,)
        return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = CohortSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)