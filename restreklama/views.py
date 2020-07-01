from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse



from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import (

	createCarSerializer,


	listSerializer,
	detailSerializer,
	imageSerializer,
	createItemSerializer,
	createPostSerializer
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
from .models import CarType, ThumbnailsImage, ItemType, ItemMy, CategoryForCar
from django_classified.models import Item, Image, Area, Group


from .pagination import PostLimitOffsetPagination, PostPageNumberPagination

from .helpers import modify_input_for_multiple_files


from django.db.models import Q


from django.shortcuts import get_object_or_404


from cars.models import DriverUser


from rest_framework.filters import (
		SearchFilter,
		OrderingFilter,
	)

from .permissions import IsOwnerOrReadOnly




class CreateCar(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated,]

	def post(self, request, format=None):
		serializer = createCarSerializer(data=request.data)

		if serializer.is_valid():
			
			user=self.request.user
			area_id = area=serializer.data['item']['area']
			area_my = Area.objects.get(pk = area_id)

			group_id = area=serializer.data['item']['group']
			group_my = Group.objects.get(pk = group_id)

			new_item = Item(
				area = area_my,
				group = group_my,
				title=serializer.data['item']['title'],
				description=serializer.data['item']['description'],
				price=serializer.data['item']['price'],
				is_active = serializer.data['item']['is_active'],
				user = user
				)
			new_item.save()



			item_type_id = serializer.data['item_type']

			if (item_type_id == 2):

				car_type_ser = request.data.get('car_type', 1)
				car_type_my = CarType.objects.get(pk = car_type_ser)
				year_ser = request.data.get('year', 1)
				cat_for_car = CategoryForCar(car_type = car_type_my, year = year_ser, item = new_item)
				cat_for_car.save()


			my_type = ItemType.objects.get(pk = item_type_id)
			new_car = ItemMy(item = new_item, item_type = my_type)
			new_car.save()



			for f in request.data.getlist('files'):
				mf = Image.objects.create(item=new_item, file=f)
				ThumbnailsImage.objects.create(image = mf, avatar_thumbnail=f)

			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CreateItem(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated,]

	def post(self, request, format=None):
		serializer = createPostSerializer(data=request.data)

		if serializer.is_valid():
			
			user=self.request.user
			area_id = area=serializer.data['item']['area']
			area_my = Area.objects.get(pk = area_id)

			group_id = area=serializer.data['item']['group']
			group_my = Group.objects.get(pk = group_id)

			new_item = Item(
				area = area_my,
				group = group_my,
				title=serializer.data['item']['title'],
				description=serializer.data['item']['description'],
				price=serializer.data['item']['price'],
				is_active = serializer.data['item']['is_active'],
				user = user
				)
			new_item.save()

			item_type_id = serializer.data['item_type']

			my_type = ItemType.objects.get(pk = item_type_id)
			new_car = ItemMy(item = new_item, item_type = my_type)
			new_car.save()



			for f in request.data.getlist('files'):
				mf = Image.objects.create(item=new_item, file=f)
				ThumbnailsImage.objects.create(image = mf, avatar_thumbnail=f)

			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ListAPIView(ListAPIView):
	serializer_class = listSerializer
	pagination_class = PostPageNumberPagination
	filter_backends= [SearchFilter, OrderingFilter]
	search_fields = ['item__title','item__description']

	def get_queryset(self, *args, **kwargs):
		queryset_list = ItemMy.objects.all().filter(item__is_active=True).order_by('-id')
		query = self.request.GET.get("area", False)
		brand = self.request.GET.get("brand", False)
		post_type = self.request.GET.get("post_type", False)
		if query:
			queryset_list = queryset_list.filter(
					Q(item__area__id__icontains=query)
					).distinct()

		#search brand and ItemMy, if item is equal show all ItemMy
		if brand:
			brand_sort = (f.item for f in CategoryForCar.objects.all().filter(car_type_id=brand))
			queryset_list = queryset_list.filter(
					Q(item__in=brand_sort)
					).distinct()

		#query_string_to_int
		if post_type:
			post_type_query = self.request.GET.get('post_type')
			post_type_converted = int(post_type_query)

			queryset_list = queryset_list.filter(
					Q(item_type__id__icontains=post_type)
				).distinct()	

		return queryset_list




class EditPost(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsOwnerOrReadOnly,]

	def put(self, request, *args, **kwargs):
		item_r_getted_id = kwargs.get('id', 'Default Value if not there')
		item_r_getted = ItemMy.objects.get(pk = item_r_getted_id)
		item_getted = item_r_getted.item


		serializer = createCarSerializer(data=request.data)

		if serializer.is_valid():
			
			user=self.request.user
			area_id = serializer.data['item']['area']
			area_my = Area.objects.get(pk = area_id)

			group_id = serializer.data['item']['group']
			group_my = Group.objects.get(pk = group_id)



			item_getted.area = area_my
			item_getted.group = group_my
			item_getted.title = serializer.data['item']['title']
			item_getted.description = serializer.data['item']['description']
			item_getted.price = serializer.data['item']['price']
			item_getted.is_active = serializer.data['item']['is_active']
			item_getted.user = user
			item_getted.save()



			item_type_id = serializer.data['item_type']
			if (item_type_id == 1):

				car_type_id = serializer.data['car_type']
				car_type_my = CarType.objects.get(pk = car_type_id)
				year_my = serializer.data['year']


				item_r_getted.item = item_getted
				item_r_getted.car_type = car_type_my
				item_r_getted.year = year_my
				item_r_getted.save()


			for f in request.data.getlist('files'):
				mf = Image.objects.create(item=item_getted, file=f)

			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def get(self, request, *args, **kwargs):
		item_r_getted_id = kwargs.get('id', '0')
		item_react = ItemMy.objects.get(pk = item_r_getted_id)
		serializer = detailSerializer(item_react)
		return Response(serializer.data)


	def delete(self, request, id):
		article = get_object_or_404(ItemMy.objects.all(), pk=id)
		article.delete()
		return Response({
			"message": "Article with id `{}` has been deleted.".format(id)
		}, status=204)



class ProfileListAPIView(ListAPIView):
	serializer_class = listSerializer
	pagination_class = PostPageNumberPagination
	filter_backends= [SearchFilter, OrderingFilter]
	search_fields = ['item__title','item__description']
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = [IsAuthenticated,]


	def get_queryset(self, *args, **kwargs):
		current_user = self.request.user
		queryset_list = ItemMy.objects.all().filter(item__is_active=True, item__user=current_user).order_by('-id')
		query = self.request.GET.get("area")
		brand = self.request.GET.get("brand")
		if query:
			queryset_list = queryset_list.filter(
					Q(item__area__id__icontains=query)
					).distinct()
		if brand:
			queryset_list = queryset_list.filter(
					Q(car_type__id__icontains=brand)
					).distinct()
		return queryset_list




class DetailApiView(RetrieveAPIView):
	queryset = ItemMy.objects.all()
	serializer_class = detailSerializer
	lookup_field = 'id'

