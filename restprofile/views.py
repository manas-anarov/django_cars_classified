from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.generics import (
	RetrieveUpdateAPIView, 
	DestroyAPIView,
	ListAPIView
	)

from django.http import JsonResponse

from .serializers import listUserSerializer
from .serializers import deleteSerializer
from .serializers import updateSerializer
from .serializers import ProfileSerializer

from rest_framework.response import Response

from cars.models import Car
from cars.models import DriverUser



from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .permissions import IsOwnerOrReadOnly



from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication



class ListAuthor(ListAPIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
	serializer_class = listUserSerializer

	def get_queryset(self, *args, **kwargs):
		return Car.objects.all().filter(profile=self.request.user)


class DeletePost(DestroyAPIView):
	queryset = Car.objects.all()
	serializer_class = deleteSerializer
	lookup_field = 'id'
	# permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Car.objects.all()
	serializer_class = updateSerializer
	lookup_field = 'id'
	# permission_classes = [IsAuthenticatedOrReadOnly]
	# permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



	




		