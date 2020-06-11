from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse


from .serializers import (
	addSerializer,
	listSerializer,
	listBrandSerializer,
	showSerializer,
	updateSerializer,
	)

from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from cars.models import Car
from cars.models import Brand


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)


from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination


class AddPost(CreateAPIView):
	serializer_class = addSerializer
	queryset = Car.objects.all()
	permission_classes = [IsAuthenticatedOrReadOnly,]
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	def perform_create(self, serializer):
		serializer.save(profile = self.request.user)


class BrandListAPIView(ListAPIView):
	serializer_class = listBrandSerializer
	queryset = Brand.objects.all()


class CarListAPIView(ListAPIView):
	serializer_class = listSerializer
	pagination_class = PostPageNumberPagination
	queryset = Car.objects.all()


class ShowPost(RetrieveAPIView):
	queryset = Car.objects.all()
	serializer_class = showSerializer
	lookup_field = 'id'


class CategoryListAPIView(ListAPIView):
	serializer_class = listSerializer

	def get_queryset(self):
		return Car.objects.filter(brand=self.kwargs['id'])




class CityListAPIView(ListAPIView):
	serializer_class = listSerializer

	def get_queryset(self):
		return Car.objects.filter(city=self.kwargs['id'])