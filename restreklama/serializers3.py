from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	ValidationError
)
from cars.models import Car
from cars.models import Brand
from cars.models import DriverUser

from django_classified.models import Item, Image, Area, Group
from .models import ItemReact, CarType
from sorl.thumbnail import get_thumbnail

from .models import ThumbnailsImage
from .models import ItemReact, CarType, ThumbnailsImage, ItemType, ItemMy

class imageSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'id',
			'item',
			'file'
		]





class TrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ['item','file']






class TaskSerializer99(serializers.HyperlinkedModelSerializer):
	title = serializers.CharField(source='item.title')
	description = serializers.CharField(source='item.description')
	price = serializers.FloatField(source='item.price')
	is_active = serializers.BooleanField(source='item.is_active')
	area_my = serializers.IntegerField()
	group_my = serializers.IntegerField()
	car_type_my = serializers.IntegerField()

	class Meta:
		model = ItemReact
		fields = [
			'area_my',
			'group_my',
			'title',
			'description',
			'price',
			'is_active',
			'car_type_my'
		]







# class createItemReactSerializer1(ModelSerializer):
# 	item = newCreateItemSerializer(required=False)
# 	class Meta:
# 		model = ItemReact
# 		fields = [
# 			'car_type',
# 			'item',
# 			'year'
# 		]


class ItemTypeSerializer(ModelSerializer):
	class Meta:
		model = ItemType
		fields = [
			'name',
			'category',
			'name'
		]













class detailSerializer(ModelSerializer):
	title = serializers.CharField(source='item.title')
	description = serializers.CharField(source='item.description')
	price = serializers.FloatField(source='item.price')
	is_active = serializers.BooleanField(source='item.is_active')
	image_first = serializers.SerializerMethodField('get_image_main')
	image_has = serializers.SerializerMethodField('get_has_image')
	images = serializers.SerializerMethodField('get_picture')
	class Meta:
		model = ItemReact
		fields = [
			'item',
			'id',
			'title',
			'description',
			'price',
			'is_active',
			'image_first',
			'image_has',
			'year',
			'car_type',
			'images'
		]

	def get_image_main(self, obj):
		all_images = Image.objects.filter(item=obj.item)
		if all_images.exists():
			big_image = Image.objects.filter(item=obj.item).first()
			sub = ThumbnailsImage.objects.filter(image = big_image).first()
			return sub.avatar_thumbnail.url

		else:
			return "/media/none/no-img.jpg"


	def get_has_image(self, obj):



		all_images = Image.objects.filter(item=obj.item)
		if all_images.exists():
			return True
		else:
			return False


	def get_picture(self, obj):

		view = self.context.get('view')
		item_r_getted_id = view.kwargs['id'] if view else None
		# print(item_r_getted_id)

		item_r_getted = ItemReact.objects.filter(pk = item_r_getted_id)
		if item_r_getted.exists():
		# if item_r_getted:
			item_r_getted = ItemReact.objects.filter(pk = item_r_getted_id).first()
			item_getted = item_r_getted.item

			all_pics = Image.objects.filter(item=item_getted)
			model2_serializer = imageSerializer(all_pics, many=True)
			return model2_serializer.data
		else:
			return "nono"

		


class createItemSerializer(ModelSerializer):
	class Meta:
		model = Item
		fields = [
			'area',
			'group',
			'title',
			'description',
			'price',
			'is_active'
		]




class addSerializer(ModelSerializer):
	class Meta:
		model = Item
		fields = [
			'area',
            'group',
            'title',
            'description',
            'price',
            'is_active'
		]


class itemSerializer(ModelSerializer):
	class Meta:
		model = Item
		fields = [
			'area',
            'group',
            'title',
            'description',
            'price',
            'is_active',
		]













class newCreateItemSerializer(ModelSerializer):
	class Meta:
		model = Item
		fields = [
			'area',
			'group',
			'title',
			'description',
			'price',
			'is_active',
		]



class createItemReactSerializer(ModelSerializer):
	item = newCreateItemSerializer(required=False)
	year = serializers.IntegerField(write_only=True)  
	car_type = serializers.IntegerField(write_only=True)  
	class Meta:
		model = ItemMy
		fields = [
			'item',
			'item_type',
			'year',
			'car_type',
		]


	def validate_car_type(self, value):
		car_type_id = value
		user_qs = CarType.objects.filter(id=car_type_id)
		if not user_qs.exists():
			raise ValidationError("CarType does  not exist")
		return value




class listSerializer(ModelSerializer):
	title = serializers.CharField(source='item.title')
	description = serializers.CharField(source='item.description')
	price = serializers.FloatField(source='item.price')
	is_active = serializers.BooleanField(source='item.is_active')
	image_has = serializers.SerializerMethodField('get_has_image')
	image_first = serializers.SerializerMethodField('get_image_main')
	class Meta:
		model = ItemMy
		fields = [
			'item',
			'id',
			'title',
			'description',
			'price',
			'is_active',
			'image_has',
			'image_first'
		]

	def get_has_image(self, obj):
		all_images = Image.objects.filter(item=obj.item)
		if all_images.exists():
			return True
		else:
			return False

	def get_image_main(self, obj):
		all_images = Image.objects.filter(item=obj.item)

		if all_images.exists():
			big_image = Image.objects.filter(item=obj.item).first()
			sub = ThumbnailsImage.objects.filter(image = big_image).first()
			return sub.avatar_thumbnail.url
		else:
			return "/media/none/no-img.jpg"




class detailItemReactSerializer(ModelSerializer):
	item = newCreateItemSerializer(required=False)
	images = serializers.SerializerMethodField('get_picture')
	class Meta:
		model = ItemReact
		fields = [
			'car_type',
			'item',
			'images'
		]

	def get_picture(self, obj):
		# item_r_getted_id =  self.kwargs['id']

		
		view = self.context.get('view')
		item_r_getted_id = view.kwargs['id'] if view else None
		print(item_r_getted_id)

		# item_r_getted_id = self.context.get('view').kwargs.get('id')
		item_r_getted = ItemReact.objects.get(pk = 100)
		item_getted = item_r_getted.item

		all_pics = Image.objects.filter(item=item_getted)
		model2_serializer = imageSerializer(all_pics, many=True)


		# star_count = Feedback.objects.filter(doctors=obj).count()

		# if all_stars.exists():
		# 	total = 0

		# 	for item in all_stars:
		# 		total = item.star + total
		# 	res_float = total / star_count
		# 	result = int(res_float)

		return model2_serializer.data
		# else:
		# 	return 0
