from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse

from .serializers import RegisterSerializer
from .serializers import ProfileSerializer
from .serializers import UserEditSerializer


from .serializers import ProfileEditSerializer

from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from cars.models import Car
from cars.models import Brand
from cars.models import DriverUser




from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication


from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import (
	AllowAny,
	)

class Register(CreateAPIView):
	permission_classes = (AllowAny,)

	serializer_class = RegisterSerializer
	queryset = DriverUser.objects.all()



class Profile(RetrieveAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	serializer_class = ProfileSerializer

	def get_object(self):
		queryset = DriverUser.objects.filter(id=self.request.user.id)
		obj = queryset[0]
		return obj


class Edit(RetrieveUpdateAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	serializer_class = UserEditSerializer

	def get_object(self):
		queryset = DriverUser.objects.filter(id=self.request.user.id)
		obj = queryset[0]
		return obj



class MyProfileAPIView(RetrieveUpdateAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	serializer_class = ProfileEditSerializer

	def get_object(self):
		queryset = DriverUser.objects.filter(id=self.request.user.id)
		obj = queryset[0]
		return obj