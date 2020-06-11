from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from cars.models import Car
from cars.models import Brand
from cars.models import DriverUser



class addSerializer(ModelSerializer):
	class Meta:
		model = Car
		fields = [
			# 'id',
			'brand',
			'title',
			'text',
			'price',
			'profile',
			'car_pic',
			'car_pic2',
			'car_pic3',
			'currency',
			'year',
			'brand',
			'city',
		]
		extra_kwargs = {"profile":
					{"read_only":True},
					}

class listBrandSerializer(ModelSerializer):
	class Meta:
		model = Brand
		fields = [
			'id',
			'id_brand',
			'name',
		]

class listSerializer(ModelSerializer):
	class Meta:
		model = Car
		fields = [
			'id',
			'brand',
			'title',
			'text',
			'price',
			'profile',
			'car_pic',
			'city',
		]

class showSerializer(ModelSerializer):
	class Meta:
		model = Car
		fields = [
			'title',
			'price',
			'text',
			'car_pic',
		]

class updateSerializer(ModelSerializer):
	class Meta:
		model = Car
		fields = [
			'id',
			# 'brand',
			'title',
			'text',
			'price',
		]