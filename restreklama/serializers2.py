from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from cars.models import Car
from cars.models import Brand
from cars.models import DriverUser

from django_classified.models import Item, Image, Area, Group
from .models import ItemReact, CarType
from sorl.thumbnail import get_thumbnail

class imageSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'id',
			'item',
			'file'
		]





# class listSerializer(ModelSerializer):
# 	# id = serializers.IntegerField(source='item.id')
# 	title = serializers.CharField(source='item.title')
# 	description = serializers.CharField(source='item.description')
# 	price = serializers.FloatField(source='item.price')
# 	is_active = serializers.BooleanField(source='item.is_active')
# 	image_has = serializers.SerializerMethodField('get_has_image')
# 	class Meta:
# 		model = ItemReact
# 		fields = [
# 			'item',
# 			'id',
# 			'title',
# 			'description',
# 			'price',
# 			'is_active',
# 			'image_has'
# 		]

# 	def get_has_image(self, obj):

# 		all_images = Image.objects.filter(item=obj.item)
# 		if all_images.exists():
# 			return True
# 		else:
# 			return False



class TrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ['item','file']

class AlbumSerializer(serializers.ModelSerializer):
	tracks = TrackSerializer(many=True)

	class Meta:
		model = Item
		fields = ['title',
			'price', 
			'tracks',
			'description',
			'is_active',
			'group',
			'user'
		]

	def create(self, validated_data):
		tracks_data = validated_data.pop('tracks')
		album = Item.objects.create(**validated_data)
		for track_data in tracks_data:
			Image.objects.create(item=album, **track_data)
		return album





class UploadSerializer(serializers.ModelSerializer):
	# item_id = serializers.IntegerField()
	# item_id = serializers.RelatedField(source='item.id', read_only=True)
	item_id = serializers.ReadOnlyField(source='item.id')

	class Meta:
		model = Image
		fields = [
			'item_id',
		]


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



class newCreateItemSerializer(ModelSerializer):
	class Meta:
		model = Item
		fields = [
			# 'id',
			'area',
			'group',
			'title',
			'description',
			'price',
			'is_active',
			# 'user'
		]



class createItemReactSerializer(ModelSerializer):
	item = newCreateItemSerializer(required=False)
	class Meta:
		model = ItemReact
		fields = [
			'car_type',
			'item',
			'year'
		]


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

from .models import ThumbnailsImage

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
		model = ItemReact
		fields = [
			'item',
			'car_type',
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



class listSerializer(ModelSerializer):
	# id = serializers.IntegerField(source='id')
	title = serializers.CharField(source='item.title')
	description = serializers.CharField(source='item.description')
	price = serializers.FloatField(source='item.price')
	is_active = serializers.BooleanField(source='item.is_active')
	image_has = serializers.SerializerMethodField('get_has_image')
	class Meta:
		model = ItemReact
		fields = [
			'item',
			'id',
			'title',
			'description',
			'price',
			'is_active',
			'image_has'
		]

	def get_has_image(self, obj):
		all_images = Image.objects.filter(item=obj.item)
		if all_images.exists():
			return True
		else:
			return False























class FileListSerializer ( serializers.Serializer ) :
	image = serializers.ListField(
		child=serializers.FileField( max_length=100000,
		allow_empty_file=False,
		use_url=False ),
		required=False
	)
	id = serializers.IntegerField(source='item.id')


	def create(self, validated_data):


		user =  self.context['request'].user
		id_new = validated_data['id']
		item = Item.objects.filter(id = id_new)


		# userprofile = Item(
		# 	area=area,
		# 	group=group,
		# 	title=validated_data['title'],
		# 	description=validated_data['description'],
		# 	price=validated_data['price'],
		# 	is_active=validated_data['is_active'],
		# 	user=user,
		# 	)
		# userprofile.save()


		images_data = self.context.get('view').request.FILES
		for img in images_data.values():
			Image.objects.create(item=item, file=img)

		return images_data




# class TaskSerializer(serializers.HyperlinkedModelSerializer):
# 	user = serializers.ReadOnlyField(source='item.id')
# 	images = imageSerializer(source='taskimage_set', many=True, read_only=True)

# 	class Meta:
# 		model = Item
# 		fields = ('user', 'images')

# 	def create(self, validated_data):
# 		images_data = self.context.get('view').request.FILES
# 		task = Item.objects.filter(id=validated_data.get('id', 'id'),
	
# 		for image_data in images_data.values():
# 			Image.objects.create(task=task, image=image_data)
# 		return task

#https://stackoverflow.com/questions/39645410/how-to-upload-multiple-files-in-django-rest-framework
class FileListSerializer ( serializers.Serializer ) :
	file = serializers.ListField(
		child=serializers.FileField( max_length=100000,
		allow_empty_file=False,
		use_url=False )
	)
	item = serializers.IntegerField()
	def create(self, validated_data):
		# blogs=Item.objects.filter(id=1)

		item = validated_data['item'],
		blogs = Item.objects.get(pk=item)

		image=validated_data.pop('file')
		for img in image:
			photo=Image.objects.create(file=img,item=blogs)
		return photo

# class PhotoSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Photo
#         read_only_fields = ("blogs",)