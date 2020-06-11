from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse



from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
	listSerializer,
	detailSerializer,
	createItemReactSerializer,
	imageSerializer,
	# FileListSerializer
	UploadSerializer
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
from .models import ItemReact, CarType
from django_classified.models import Item, Image, Area, Group


# from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination

from .helpers import modify_input_for_multiple_files


from django.db.models import Q

#https://stackoverflow.com/questions/39645410/how-to-upload-multiple-files-in-django-rest-framework
# class AddPost(CreateAPIView):
# 	serializer_class = FileListSerializer
# 	parser_classes = (MultiPartParser, FormParser,)
# 	queryset=Image.objects.all()



from cars.models import DriverUser


#неудачная попытка сохранить фото в одном посте
# class AddPost(CreateAPIView):
# 	serializer_class = TaskSerializer
# 	parser_classes = (MultiPartParser, FormParser,)
# 	queryset=ItemReact.objects.all()
# 	authentication_classes = (TokenAuthentication, SessionAuthentication)

# 	def perform_create(self, serializer):

# 		area_id = area=serializer.data['area_my']
# 		area_my = Area.objects.get(pk = area_id)

# 		group_id = area=serializer.data['group_my']
# 		group_my = Group.objects.get(pk = group_id)

# 		user=self.request.user

# 		new_item = Item(
# 			area=area_my,
# 			group=group_my,
# 			title=serializer.data['title'],
# 			description=serializer.data['description'],
# 			price=serializer.data['price'],
# 			is_active = serializer.data['is_active'],
# 			user = user
# 			)
# 		new_item.save()

# 		car_type_id = serializer.data['car_type_my']
# 		car_type_my = CarType.objects.get(pk = car_type_id)

# 		item_for_react = Item.objects.get(pk = new_item.pk)

# 		new_item_react = ItemReact(
# 			item = item_for_react, 
# 			car_type = car_type_my
# 			)
# 		new_item_react.save


# 		for f in self.request.data.getlist('files'):
# 			mf = Image.objects.create(item=item_for_react, file=f)





class AddPost(APIView):
	authentication_classes = (TokenAuthentication, SessionAuthentication)

	def post(self, request, format=None):
		serializer = createItemReactSerializer(data=request.data)

		if serializer.is_valid():
			
			user=self.request.user
			area_id = area=serializer.data['item']['area']
			area_my = Area.objects.get(pk = area_id)

			group_id = area=serializer.data['item']['group']
			group_my = Group.objects.get(pk = group_id)

			new_item = Item(
				# area=serializer.data['item']['area'],
				area = area_my,
				# group=serializer.data['item']['group'],
				group = group_my,
				title=serializer.data['item']['title'],
				description=serializer.data['item']['description'],
				price=serializer.data['item']['price'],
				is_active = serializer.data['item']['is_active'],
				user = user
				)
			new_item.save()

			car_type_id = serializer.data['car_type']
			car_type_my = CarType.objects.get(pk = car_type_id)


			new_item_react = ItemReact(
				item = new_item, 
				car_type = car_type_my
				)
			new_item_react.save()

			for f in request.data.getlist('files'):
				mf = Image.objects.create(item=new_item, file=f)

			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# class AddPost(CreateAPIView):
# 	serializer_class = createItemReactSerializer
# 	queryset=ItemReact.objects.all()
# 	authentication_classes = (TokenAuthentication, SessionAuthentication)



#https://stackoverflow.com/questions/48756249/django-rest-uploading-and-serializing-multiple-images
#https://stackoverflow.com/questions/39645410/how-to-upload-multiple-files-in-django-rest-framework/45618675
class UploadImage(CreateAPIView):
	serializer_class = UploadSerializer
	parser_classes = (MultiPartParser, FormParser,)
	queryset=Image.objects.all()

	def perform_create(self, serializer):

		item_id = serializer.data['item_id']
		item = Item.objects.get(pk = item_id)
		# for f in self.request.data.getlist('files'):
		for f in self.request.data.getlist('image'):
			mf = Image.objects.create(item=item, file=f)

			

# class AddPost(CreateAPIView):
# 	serializer_class = imageSerializer
# 	queryset=Image.objects.all()
# 	authentication_classes = (TokenAuthentication, SessionAuthentication)



# class AddPost(CreateAPIView):
# 	serializer_class = FileListSerializer
# 	parser_classes = (MultiPartParser, FormParser,)
# 	queryset=Item.objects.all()
# 	authentication_classes = (TokenAuthentication, SessionAuthentication)




class ListAPIView(ListAPIView):
	serializer_class = listSerializer
	pagination_class = PostPageNumberPagination
	
	def get_queryset(self):
		return ItemReact.objects.filter(item__is_active=True)

	def get_queryset(self, *args, **kwargs):
		queryset_list = ItemReact.objects.all().filter(item__is_active=True).order_by('id')
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


class ShowPost(RetrieveAPIView):
	queryset = ItemReact.objects.all()
	serializer_class = detailSerializer
	lookup_field = 'id'



#https://stackoverflow.com/questions/52903232/how-to-upload-multiple-images-using-django-rest-framework
# class AddPost(APIView):
# 	parser_classes = (MultiPartParser, FormParser)

# 	def get(self, request):
# 		all_images = Image.objects.all()
# 		serializer = imageSerializer(all_images, many=True)
# 		return JsonResponse(serializer.data, safe=False)

# 	def post(self, request, *args, **kwargs):

# 		# property_id = request.POST.get('item', 1)
# 		property_id = request.data['item']

# 		# converts querydict to original dict
# 		images = dict((request.data).lists())['file']
# 		flag = 1
# 		arr = []
# 		for img_name in images:
# 			modified_data = modify_input_for_multiple_files(property_id,
#                                                             img_name)
# 			file_serializer = imageSerializer(data=modified_data)
# 			if file_serializer.is_valid():
# 				file_serializer.save()
# 				arr.append(file_serializer.data)
# 			else:
# 				flag = 0

# 		if flag == 1:
# 			return Response(arr, status=status.HTTP_201_CREATED)
# 		else:
# 			return Response(arr, status=status.HTTP_400_BAD_REQUEST)