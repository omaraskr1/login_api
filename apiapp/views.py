from django.shortcuts import render
from rest_framework import viewsets
from .models import awsimage
from .serliazer import awsiImageserliazer,UserSignupsrilaizer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
import joblib
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
import json
import numpy as np
# from sklearn import preprocessing
# import pandas as pd
# Create your views here.
class awsImageview(viewsets.ModelViewSet):
    # image=viewsets.ModelViewSet.get_serializer['image']
    # print(image)
    queryset=awsimage.objects.all()
    serializer_class=awsiImageserliazer
@api_view(["POST"])
def approvereject(request):
	try:
		mdl=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/loan_model.pkl")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		mydata=request.data
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		scalers=joblib.load("/Users/sahityasehgal/Documents/Coding/DjangoApiTutorial/DjangoAPI/MyAPI/scalers.pkl")
		X=scalers.transform(unit)
		y_pred=mdl .predict(X)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		return JsonResponse('Your Status is {}'.format(newdf), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
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