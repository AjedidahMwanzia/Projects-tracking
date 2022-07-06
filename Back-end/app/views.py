
from django.shortcuts import redirect, render
from django.contrib import messages

from app.forms import UserRegistrationForm
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api
from .forms import UserRegistrationForm, UserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from app.permissions import IsAdminOrReadOnly
from .models import  Profile,Project,Cohort, User
from .serializers import ProfileSerializer, UserSerializer,ProjectSerializer, CohortSerializer
from rest_framework import status
import jwt,datetime
from .forms import *


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
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user=User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found')

        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')


        payload = {
            'id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=120),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data ={
            'jwt': token
        }

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated')




        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)



 
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response= Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'come again soon'
        }

        return response 

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProfileList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
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