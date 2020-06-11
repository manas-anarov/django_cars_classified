from django.db import models
from django_classified.models import Item, Image
from sorl.thumbnail import ImageField
from django.utils.translation import ugettext as _

from django.contrib.contenttypes.models import ContentType




# class Item(models.Model):
#     image = ImageField(upload_to='whatever')


class CarType(models.Model):
	name = models.CharField(_('name'), max_length=100)

	def __str__(self):
		return self.name


class ItemReact(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
	year = models.PositiveSmallIntegerField(blank=True, null=True)



class ItemType(models.Model):
	category = models.ManyToManyField(ContentType)
	name = models.CharField(_('name'), max_length=100)

	def __str__(self):
		return self.name


class ItemMy(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)




class CategoryForCar(models.Model):
	car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
	year = models.PositiveSmallIntegerField(blank=True, null=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)






from imagekit.models import ProcessedImageField
from sorl.thumbnail import ImageField
from imagekit.processors import ResizeToFill

class ThumbnailsImage(models.Model):
	image = models.ForeignKey(Image, on_delete=models.CASCADE)
	avatar_thumbnail = ProcessedImageField(upload_to='avatars',
											processors=[ResizeToFill(250, 150)],
											format='JPEG',
											options={'quality': 60})