from django.shortcuts import render
from rest_framework import viewsets
from .models import awsimage
from .serliazer import awsiImageserliazer,UserSignupsrilaizer
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
# Create your views here.
class awsImageview(viewsets.ModelViewSet):
    queryset=awsimage.objects.all()
    serializer_class=awsiImageserliazer

# class UserLoginViewset(viewsets.ModelViewSet):
#     permission_classes=(IsAuthenticated,)
#     serializer_class=UserLoginserliazer
#     queryset=get_user_model().objects.all()


class userSignupViewset(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=UserSignupsrilaizer



# 
from .serliazer import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer