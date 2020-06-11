from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from cars.models import Car
from cars.models import Brand
from cars.models import DriverUser

from django_classified.models import Item, Image, Area, Group
from .models import ItemReact




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




class imageSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'item',
			'file'
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


# class listSerializer(ModelSerializer):
# 	class Meta:
# 		model = ItemReact
# 		fields = [
# 			'area',
# 			'group',
# 			'title',
# 			'description',
# 			'price',
# 			'is_active',
# 			'id',
# 		]


class listSerializer(ModelSerializer):
	id = serializers.IntegerField(source='item.id')
	title = serializers.CharField(source='item.title')
	description = serializers.CharField(source='item.description')
	price = serializers.FloatField(source='item.price')
	is_active = serializers.BooleanField(source='item.is_active')
	class Meta:
		model = ItemReact
		fields = [
			'item',
			'id',
			'title',
			'description',
			'price',
			'is_active'
		]







class detailSerializer(ModelSerializer):
	id = serializers.IntegerField(source='item.id')
	title = serializers.CharField(source='item.title')
	description = serializers.CharField(source='item.description')
	price = serializers.FloatField(source='item.price')
	is_active = serializers.BooleanField(source='item.is_active')
	image_first = serializers.SerializerMethodField('get_image_main')
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
			'image_first',
			'image_has'
		]

	def get_image_main(self, obj):

		all_images = Image.objects.filter(item=obj.item)
		if all_images.exists():
			return Image.objects.filter(item=obj.item).first().file.url
		else:
			return "/media/none/no-img.jpg"


	def get_has_image(self, obj):

		all_images = Image.objects.filter(item=obj.item)
		if all_images.exists():
			return True
		else:
			return False






# class ListingSerializer(serializers.HyperlinkedModelSerializer):
#     user = UsernameSerializer(read_only=True)
#     image_set = ImageSerializerForListingDetail(many=True, required=False)    

#     class Meta:
#         model = Listing
#         exclude = ('url', )
#         depth = 1  
  
#     def create(self, validated_data):
#         images_data = self.context.get('view').request.FILES
#         listing = Listing.objects.create(**validated_data)
#         for image_data in images_data.values():
#             Image.objects.create(photo=image_data, listing=listing)
#         return listing    




class reactSerializer(ModelSerializer):
	class Meta:
		model = ItemReact
		fields = [
			'car_type',
		]







class ItemReactSerializer(serializers.HyperlinkedModelSerializer):
# class ItemReactSerializer(ModelSerializer):
	# item = itemSerializer(required=False)
	image_set = imageSerializer(many=True, required=False)
	# react_item = reactSerializer(required=False)    
	# file1 = serializers.ImageField(required=False,allow_empty_file=True)
	# file2 = serializers.ImageField(required=False)
	# file3 = serializers.ImageField(required=False)
	class Meta:
		model = ItemReact
		fields = [
			# 'item',
			# 'react_item',
			'image_set',
		]
		depth = 1

	def create(self, validated_data):



		images_data = self.context.get('view').request.FILES
		for image_data in images_data.values():
			Image.objects.create(item=1, file=image_data)


		return doctor





class FileListSerializer (serializers.Serializer) :
	image = serializers.ListField(
		child=serializers.FileField( max_length=100000,
		allow_empty_file=False,
		use_url=False )
	)
	item = itemSerializer(required=False)
	def create(self, validated_data):

		item_data = validated_data.pop('item')
		user =  self.context['request'].user
		item_for_db = Item(
			area=item_data['area'],
			group=item_data['group'],
			title=item_data['title'],
			description=item_data['description'],
			price=item_data['price'],
			is_active=item_data['is_active'],
			user=user,
			)
		item_for_db.save()


		# blogs=Blogs.objects.latest('created_at')
		image=validated_data.pop('image')
		for img in image:
			photo=image.objects.create(image=img,item=item_for_db)
		return photo






class FileListSerializer88(serializers.HyperlinkedModelSerializer):
	images = imageSerializer( many=True, read_only=True)
	item = itemSerializer(required=False)
	class Meta:
		model = Item
		fields = ('images','item')
	def create(self, validated_data):

		item_data = validated_data.pop('item')
		user =  self.context['request'].user
		item_for_db = Item(
			area=item_data['area'],
			group=item_data['group'],
			title=item_data['title'],
			description=item_data['description'],
			price=item_data['price'],
			is_active=item_data['is_active'],
			user=user,
			)
		item_for_db.save()
		
		images_data = self.context.get('view').request.FILES
		for file_db in file_db.values():
			Image.objects.create(item=item_for_db, file=image_db)
		return item_for_db






class ItemReactSerializer1(serializers.HyperlinkedModelSerializer):
# class ItemReactSerializer(ModelSerializer):
	item = itemSerializer(required=False)
	image_set = imageSerializer(many=True, required=False)
	react_item = reactSerializer(required=False)    
	# file1 = serializers.ImageField(required=False,allow_empty_file=True)
	# file2 = serializers.ImageField(required=False)
	# file3 = serializers.ImageField(required=False)
	class Meta:
		model = ItemReact
		fields = [
			'item',
			'react_item',
			'image_set',
		]
		depth = 1

	def create(self, validated_data):

		user_data = validated_data.pop('item')
		user =  self.context['request'].user
		userprofile = Item(
			area=user_data['area'],
			group=user_data['group'],
			title=user_data['title'],
			description=user_data['description'],
			price=user_data['price'],
			is_active=user_data['is_active'],
			user=user,
			)
		userprofile.save()
		
		# validated_data['file1']:
		# salam = validated_data['file1'];


		images_data = self.context.get('view').request.FILES
		for image_data in images_data.values():
			Image.objects.create(item=userprofile, file=image_data)

		# image_one = Image(item=userprofile, file =validated_data['file1'])
		# image_one.save()

		# image_two = Image(item=userprofile, file = validated_data['file2'])
		# image_three = Image(item=userprofile, file = validated_data['file3'])
		
		
		# image_two.save()
		# image_three.save()


		react_data = validated_data.pop('react_item')

		doctor = ItemReact(
			item=userprofile,
			car_type=react_data['car_type'],
			)
		doctor.save()


		return doctor








class FileListSerializer1 (serializers.Serializer ) :
	image = serializers.ListField(
		child=serializers.ImageField( max_length=100000,
		allow_empty_file=False,
		use_url=False )
	)
	item = itemSerializer(required=False)

	def create(self, validated_data):

		user =  self.context['request'].user

		# area = Area(slug="asasaas", "title")
		area = Area.objects.first()
		group = Group.objects.first()

		userprofile = Item(
			area=area,
			group=group,
			title="s",
			description="S",
			price=1,
			is_active=True,
			user=user,
			)
		userprofile.save()



		# blogs=Blogs.objects.latest('created_at')
		image=validated_data.pop('image')
		for img in image:
			#photo=Photo.objects.create(image=img,blogs=blogs,**validated_data)
			photo = Image.objects.create(item=userprofile, file=img)
		return photo






class FileListSerializer99 (serializers.Serializer ) :
	image = serializers.ListField(
		child=serializers.ImageField( max_length=100000,
		allow_empty_file=False,
		use_url=False )
	)
	item = itemSerializer(required=False)
	# first_name = serializers.CharField(source='user.first_name')

	def create(self, validated_data):

		user_data = validated_data.pop('item')
		user =  self.context['request'].user
		userprofile = Item(
			area=user_data['area'],
			group=user_data['group'],
			title=user_data['title'],
			description=user_data['description'],
			price=user_data['price'],
			is_active=user_data['is_active'],
			user=user,
			)
		userprofile.save()


		image=validated_data.pop('image')
		for img in image:
			photo = Image.objects.create(item=userprofile, file=img)
		return photo





class PhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemReact
		read_only_fields = ("blogs",)





# class TrackSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Track
# 		fields = ['order', 'title', 'duration']

class FileListSerializer2(serializers.Serializer ):
	image = imageSerializer(many=True)

	class Meta:
		model = ItemReact
		fields = ['file1']

	def create(self, validated_data):
		tracks_data = validated_data.pop('image')
		album = ItemReact.objects.create(**validated_data)
		for track_data in tracks_data:
			Image.objects.create(album=album, **track_data)
		return album





# class FileListSerializer3(serializers.HyperlinkedModelSerializer) :
# 	salam = serializers.ListField(
# 	child=serializers.FileField( max_length=100000,
# 		allow_empty_file=False,
# 		use_url=False )
# 	)
# 	item = itemSerializer(required=False)

# 	class Meta:
# 		model = ItemReact
# 		fields = ['salam', 'item']

# 	def create(self, validated_data):

# 		user_data = validated_data.pop('item')
# 		user =  self.context['request'].user
# 		userprofile = Item(
# 			area=user_data['area'],
# 			group=user_data['group'],
# 			title=user_data['title'],
# 			description=user_data['description'],
# 			price=user_data['price'],
# 			is_active=user_data['is_active'],
# 			user=user,
# 			)
# 		userprofile.save()


# 		image=validated_data.pop('salam')
# 		for img in image:
# 			photo=Image.objects.create(file=img, item=userprofile)
# 		return photo







class ImageSerializer(serializers.HyperlinkedModelSerializer):
	item = itemSerializer(required=False)
	area = serializers.SlugRelatedField(queryset=Area.objects.all(), slug_field='area')
	group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='group')
	title = serializers.CharField(max_length=300)
	description = serializers.CharField(max_length=300)
	price = serializers.CharField(max_length=400)
	is_active = serializers.BooleanField()

	# group = serializers.CharField(source='user.group')
	class Meta:
		model = Image
		fields = [
			'item',
			'image'
		]





# class WorkSerializer(serializers.Serializer ) :
# 	image = serializers.ListField(
# 		child=serializers.ImageField( max_length=100000,
# 		allow_empty_file=False,
# 		use_url=False,
# 		),
# 		required=False
# 	)
# 	# area = serializers.SlugRelatedField(queryset=Area.objects.all(), slug_field='area', required=False)
# 	# group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='group')
# 	title = serializers.CharField(max_length=300)
# 	description = serializers.CharField(max_length=300)
# 	price = serializers.CharField(max_length=400)
# 	is_active = serializers.BooleanField()

# 	class Meta:
# 		model = Image
# 		fields = [
# 			# 'area',
# 			# 'group',
# 			'title',
# 			'description',
# 			'price',
# 			'is_active',
# 		]

# 	def create(self, validated_data):

# 		user =  self.context['request'].user

# 		# area = Area(slug="asasaas", "title")
# 		area = Area.objects.first()
# 		group = Group.objects.first()
# 		# area = validated_data['area']
# 		# group = validated_data['group']
# 		title = validated_data['title']
# 		description = validated_data['description']
# 		price = validated_data['price']
# 		is_active = validated_data['is_active']

# 		userprofile = Item(
# 			area=area,
# 			group=group,
# 			title=title,
# 			description=description,
# 			price=price,
# 			is_active=is_active,
# 			user=user,
# 			)
# 		userprofile.save()



# 		# blogs=Blogs.objects.latest('created_at')
# 		image=validated_data.pop('image')
# 		for img in image:
# 			#photo=Photo.objects.create(image=img,blogs=blogs,**validated_data)
# 			photo = Image.objects.create(item=userprofile, file=img)
# 		return photo






class AnimalSerializer(serializers.HyperlinkedModelSerializer):

	# images = imageSerializer(many=True, read_only=True)
	images = imageSerializer(many=True, read_only=True)
	# area = serializers.SlugRelatedField(queryset=Area.objects.all(), slug_field='area', required=False)
	salam = serializers.IntegerField(read_only=True)
	palam = serializers.IntegerField(read_only=True)
	# group = serializers.IntegerField()
	# group = serializers.SlugRelatedField(queryset=Group.objects.all(), slug_field='group', required=False)
	# price = serializers.IntegerField()


	def create(self, validated_data):


		# area = Area(slug="asasaas", "title")
		area_db = Area.objects.get(pk=validated_data['salam'])
		group_db = Group.objects.get(pk=validated_data['palam'])
		title = validated_data['title']
		description = validated_data['description']
		price = validated_data['price']
		is_active = validated_data['is_active']
		user =  self.context['request'].user

		userprofile = Item(
			area=area_db,
			group=group_db,
			title=title,
			description=description,
			price=price,
			is_active=is_active,
			user=user,
			)
		userprofile.save()



		images_data = self.context['request'].FILES
		# animal = Item.objects.create(
		# 	title=validated_data.get('title', 'default-title')
		# )
		for image_data in images_data.getlist('file'):
			Image.objects.create(item=userprofile, image=image_data)
		return userprofile

	class Meta:
		model = Item
		# lookup_field = 'slug'
		# extra_kwargs = {
		# 	{'url': {'lookup_field': 'slug'}
		# }
		fields = [
			'images',
			'title',
			'description',
			'is_active',
			'palam',
			'salam',
			'price'
		]




class TaskSerializer(serializers.HyperlinkedModelSerializer):
	title = serializers.ReadOnlyField(source='item.title')
	images = imageSerializer(source='taskimage_set', many=True, read_only=True)

	class Meta:
		model = Image
		fields = ('item', 'images', 'title')

	def create(self, validated_data):
		images_data = self.context.get('view').request.FILES
		task = Task.objects.create(title=validated_data.get('title', 'no-title'),
			user_id=1)
		for image_data in images_data.values():
			TaskImage.objects.create(task=task, image=image_data)
		return task







	# item_for_db = Item(
	# 		area=item_data['area'],
	# 		group=item_data['group'],
	# 		title=item_data['title'],
	# 		description=item_data['description'],
	# 		price=item_data['price'],
	# 		is_active=item_data['is_active'],
	# 		user=user,
	# 		)



# class PhotoSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = Photo
# 		read_only_fields = ("blogs",)



# class ItemReactSerializer(ModelSerializer):
# 	item = itemSerializer(required=False)
# 	file1 = serializers.ImageField(required=False,allow_empty_file=True)
# 	file2 = serializers.ImageField(required=False)
# 	file3 = serializers.ImageField(required=False)
# 	class Meta:
# 		model = ItemReact
# 		fields = [
# 			'item',
# 			'car_type',
# 			'file1',
# 			'file2',
# 			'file3',
# 		]

# 	def create(self, validated_data):

# 		user_data = validated_data.pop('item')
# 		user =  self.context['request'].user
# 		userprofile = Item(
# 			area=user_data['area'],
# 			group=user_data['group'],
# 			title=user_data['title'],
# 			description=user_data['description'],
# 			price=user_data['price'],
# 			is_active=user_data['is_active'],
# 			user=user,
# 			)
# 		userprofile.save()
		
# 		# validated_data['file1']:
# 		salam = validated_data['file1'];

# 		image_one = Image(item=userprofile, file =validated_data['file1'])
# 		image_one.save()

# 		image_two = Image(item=userprofile, file = validated_data['file2'])
# 		image_three = Image(item=userprofile, file = validated_data['file3'])
		
		
# 		image_two.save()
# 		image_three.save()

# 		doctor = ItemReact(
# 			item=userprofile,
# 			car_type=validated_data['car_type'],
# 			)
# 		doctor.save()


# 		return doctor




# https://stackoverflow.com/questions/39645410/how-to-upload-multiple-files-in-django-rest-framework
# https://stackoverflow.com/questions/39440153/error-while-saving-image-using-django-rest-framework-with-angularjs


class FileListSerializer ( serializers.Serializer ) :
	image = serializers.ListField(
		child=serializers.FileField( max_length=100000,
		allow_empty_file=False,
		use_url=False ),
		required=False
	)
	# area = serializers.IntegerField()
	# group = serializers.IntegerField()
	title = serializers.CharField(max_length=300)
	description = serializers.CharField(max_length=300)
	price = serializers.CharField(max_length=400)
	is_active = serializers.BooleanField()

	def create(self, validated_data):


		area = Area.objects.first()
		group = Group.objects.first()


		user =  self.context['request'].user
		userprofile = Item(
			area=area,
			group=group,
			title=validated_data['title'],
			description=validated_data['description'],
			price=validated_data['price'],
			is_active=validated_data['is_active'],
			user=user,
			)
		userprofile.save()


		images_data = self.context.get('view').request.FILES
		for img in images_data.values():
			Image.objects.create(item=userprofile, file=img)

		return images_data









class newCreateItemSerializer(ModelSerializer):
	class Meta:
		model = Item
		fields = [
			'id',
			'area',
			'group',
			'title',
			'description',
			'price',
			'is_active',
			'user'
		]


class createItemReactSerializer(ModelSerializer):
	item = createItemSerializer(required=False)
	class Meta:
		model = ItemReact
		fields = [
			'car_type',
			'item',
		]

	def create(self, validated_data):
		item_data = validated_data.pop('item')
		user =  self.context['request'].user
		new_item = Item(
			area=item_data['area'],
			group=item_data['group'],
			title=item_data['title'],
			description=item_data['description'],
			price=item_data['price'],
			is_active = item_data['is_active'],
			user = user
			)
		new_item.save()


		new_item_react = ItemReact(
			item=new_item,
			car_type=validated_data['car_type'],
			)
		new_item_react.save()


		return new_item_react