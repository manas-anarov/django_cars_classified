from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	ValidationError
)
from cars.models import Car
from cars.models import Brand
from cars.models import DriverUser

from django_classified.models import Item, Image, Area, Group
from .models import CarType
from sorl.thumbnail import get_thumbnail

from .models import ThumbnailsImage
from .models import CarType, ThumbnailsImage, ItemType, ItemMy, CategoryForCar

from django.conf import settings



class imageSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'id',
			'item',
			'file'
		]



class ItemTypeSerializer(ModelSerializer):
	class Meta:
		model = ItemType
		fields = [
			'name',
			'category',
			'name'
		]



class imageSliderSerializer(ModelSerializer):
	original = serializers.SerializerMethodField()
	thumbnail = serializers.SerializerMethodField()
	class Meta:
		model = Image
		fields = [
			'original',
			'thumbnail',
			'id'
		]

	def get_original(self, obj):
		all_images = Image.objects.filter(pk=obj.id)
		if all_images.exists():
			big_image = Image.objects.filter(pk=obj.id).first()
			final_image_url = settings.SITE_URL_FOR_IMAGE + big_image.file.url
			return final_image_url

		else:
			return "/media/none/no-img.jpg"


	def get_thumbnail(self, obj):
		all_images = Image.objects.filter(pk=obj.id)
		if all_images.exists():
			big_image = Image.objects.filter(pk=obj.id).first()
			sub = ThumbnailsImage.objects.filter(image = big_image).first()

			final_image_url = settings.SITE_URL_FOR_IMAGE + sub.avatar_thumbnail.url
			return final_image_url
		else:
			return "/media/none/no-img.jpg"




class detailSerializer(ModelSerializer):
	title = serializers.CharField(source='item.title')
	description = serializers.CharField(source='item.description')
	price = serializers.FloatField(source='item.price')
	is_active = serializers.BooleanField(source='item.is_active')
	image_first = serializers.SerializerMethodField('get_image_main')
	image_has = serializers.SerializerMethodField('get_has_image')
	images = serializers.SerializerMethodField('get_picture')
	year = serializers.SerializerMethodField()
	# car_type = serializers.SerializerMethodField()
	car_type_name = serializers.SerializerMethodField()
	images_slider = serializers.SerializerMethodField()
	class Meta:
		model = ItemMy
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
			# 'car_type',
			'car_type_name',
			'images',
			'images_slider',
			'item_type'
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

		item_r_getted = ItemMy.objects.filter(pk = item_r_getted_id)
		if item_r_getted.exists():
			item_r_getted = ItemMy.objects.filter(pk = item_r_getted_id).first()
			item_getted = item_r_getted.item

			all_pics = Image.objects.filter(item=item_getted)
			model2_serializer = imageSerializer(all_pics, many=True)
			return model2_serializer.data
		else:
			return None


	def get_year(self, obj):
		if (obj.item_type.id == 2):
			try:
				cat_for_car = CategoryForCar.objects.get(item=obj.item)
			except ObjectDoesNotExists:
				return None
			else:
				return cat_for_car.year

		if (obj.item_type != 2):
			return None

	# def get_car_type(self, obj):
	# 	if (obj.item_type.id == 2):
	# 		all_images = CategoryForCar.objects.get(item=obj.item)
	# 		return all_images.car_type.id
	# 	if (obj.item_type != 2):
	# 		return None

	def get_car_type_name(self, obj):
		if (obj.item_type.id == 2):
			try:
				cat_for_car = CategoryForCar.objects.get(item=obj.item)
			except ObjectDoesNotExists:
				return None
			else:
				return cat_for_car.car_type.name
		if (obj.item_type.id != 2):
			return None


	def get_images_slider(self, obj):
		view = self.context.get('view')
		item_r_getted_id = view.kwargs['id'] if view else None

		item_r_getted = ItemMy.objects.filter(pk = item_r_getted_id)
		if item_r_getted.exists():
			item_r_getted = ItemMy.objects.filter(pk = item_r_getted_id).first()
			item_getted = item_r_getted.item

			all_pics = Image.objects.filter(item=item_getted)
			model2_serializer = imageSliderSerializer(all_pics, many=True)

			return model2_serializer.data
		else:
			return None

		


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




class createCarSerializer(ModelSerializer):
	item = newCreateItemSerializer(required=False)
	year = serializers.IntegerField(write_only=True, required=False)  
	car_type = serializers.IntegerField(write_only=True, required=False)
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





class createPostSerializer(ModelSerializer):
	item = newCreateItemSerializer(required=False)
	class Meta:
		model = ItemMy
		fields = [
			'item',
			'item_type',
		]





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
