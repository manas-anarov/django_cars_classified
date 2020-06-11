from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse



from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
	FileListSerializer,
	addSerializer,
	ItemReactSerializer,
	itemSerializer,
	ImageSerializer,
	AnimalSerializer,
	TaskSerializer,
	listSerializer,
	detailSerializer,
	createItemSerializer,
	createItemReactSerializer
	# listBrandSerializer,
	# showSerializer,
	# updateSerializer,
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
from .models import ItemReact, Image, Item


# from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination


# class AddPost(CreateAPIView):
# 	serializer_class = addSerializer
# 	queryset = Car.objects.all()
# 	# permission_classes = [IsAuthenticatedOrReadOnly,]
# 	authentication_classes = (TokenAuthentication, SessionAuthentication)
# 	def perform_create(self, serializer):
# 		serializer.save(profile = self.request.user)





class AddPost(CreateAPIView):
	serializer_class = createItemReactSerializer
	queryset=ItemReact.objects.all()
	authentication_classes = (TokenAuthentication, SessionAuthentication)



# https://stackoverflow.com/questions/39645410/how-to-upload-multiple-files-in-django-rest-framework
# class AddPost(CreateAPIView):
# 	serializer_class = FileListSerializer
# 	parser_classes = (MultiPartParser, FormParser,)
# 	queryset=Item.objects.all()
# 	authentication_classes = (TokenAuthentication, SessionAuthentication)

# 	def perform_create(self, serializer):
# 		serializer.save(user = self.request.user)



class AddPost33(CreateAPIView):
	serializer_class = TaskSerializer
	queryset = Item.objects.all()
	parser_classes = (JSONParser, MultiPartParser, FormParser)
	# permission_classes = [IsAuthenticatedOrReadOnly,]
	authentication_classes = (TokenAuthentication, SessionAuthentication)



class AddPost41(CreateAPIView):
	serializer_class = AnimalSerializer
	queryset = Item.objects.all()
	parser_classes = (JSONParser, MultiPartParser, FormParser)
	# permission_classes = [IsAuthenticatedOrReadOnly,]
	authentication_classes = (TokenAuthentication, SessionAuthentication)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)


class AddPost2(CreateAPIView):
	serializer_class = itemSerializer
	parser_classes = (MultiPartParser, FormParser,)

	permission_classes = [IsAuthenticatedOrReadOnly,]
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	queryset = Item.objects.all()

	def perform_create(self, serializer):
		salam = serializer.save(user = self.request.user)

		for f in self.request.data.getlist('files'):
			mf = Image.objects.create(file=f, item = salam)
			print(mf)
			salam.files.add(mf)



class AddPost3(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def get(self, request):
		all_images = Image.objects.all()
		serializer = ImageSerializer(all_images, many=True)
		return JsonResponse(serializer.data, safe=False)

	def post(self, request, *args, **kwargs):
		property_id = request.data['item.id']

        # converts querydict to original dict
		images = dict((request.data).lists())['image']
		flag = 1
		arr = []
		for img_name in images:
			modified_data = modify_input_for_multiple_files(property_id,
			img_name)
			file_serializer = ImageSerializer(data=modified_data)
			if file_serializer.is_valid():
				file_serializer.save()
				arr.append(file_serializer.data)
			else:
				flag = 0

		if flag == 1:
			return Response(arr, status=status.HTTP_201_CREATED)
		else:
			return Response(arr, status=status.HTTP_400_BAD_REQUEST)




	# def create(self, request):

	# 	data = request.data

	# 	serializer = itemSerializer(data=request.data)
	# 	if serializer.is_valid():
 #            # device = serializer.save()

	# 		obj = serializer.save()
	# 		for f in self.request.data.getlist('files'):
	# 			mf = Image.objects.create(file=f, item = obj)
	# 		obj.files.add(mf)



	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	else:
	# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def perform_create(self, serializer):
#         project = serializer.data['project']
#         if project in self.request.user.projects.all():
#             serializer.save(project=project)
#         else:
#             raise exceptions.PermissionDenied


# class BrandListAPIView(ListAPIView):
# 	serializer_class = listBrandSerializer
# 	queryset = Brand.objects.all()


class ListAPIView(ListAPIView):
	serializer_class = listSerializer
	pagination_class = PostPageNumberPagination
	
	def get_queryset(self):
		return ItemReact.objects.filter(item__is_active=True)


class ShowPost(RetrieveAPIView):
	queryset = ItemReact.objects.all()
	serializer_class = detailSerializer
	lookup_field = 'id'


# class CategoryListAPIView(ListAPIView):
# 	serializer_class = listSerializer

# 	def get_queryset(self):
# 		return Car.objects.filter(brand=self.kwargs['id'])




# class CityListAPIView(ListAPIView):
# 	serializer_class = itemSerializer

# 	def get_queryset(self):
# 		return Item.objects.filter(city=self.kwargs['id'])