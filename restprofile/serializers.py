from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from cars.models import Car
from cars.models import Brand
from cars.models import DriverUser

class listUserSerializer(ModelSerializer):
	class Meta:
		model = Car
		fields = [
			'id',
			'brand',
			'title',
			'text',
			'price',
			'car_pic',
		]


class deleteSerializer(ModelSerializer):
	class Meta:
		model = Car
		fields = [
			'id',
		]


class updateSerializer(ModelSerializer):
	class Meta:
		model = Car
		fields = [
			# 'brand',
			'title',
			'text',
			'price',
			'currency',
			'car_pic',
		]



class ProfileSerializer(ModelSerializer):
	class Meta:
		model = DriverUser
		fields = [
			'id',
			'name',
			'tel',
			'image',
			'first_name',
			'last_name'
		]