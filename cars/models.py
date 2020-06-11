from django.db import models
from django.contrib.auth.models import AbstractUser



LABEL_CHOICES = (
    (1, 'сом'),
    (2, '$'),
    (3, 'руб')
)

CITY_CHOICES = (
    (1, 'Чуй'),
    (2, 'Ош'),
    (3, 'Джалал-Абад'),
    (4, 'Ыссык Кол'),
    (5, 'Нарын'),
    (6, 'Талас'),
    (7, 'Баткен'),
)

class Brand(models.Model):
	id_brand = models.IntegerField(default=0)
	name = models.CharField(max_length=400, default=0)

	def __str__(self):
		return self.name




class DriverUser(AbstractUser):
	name = models.CharField(max_length=250, default='Name')
	image = models.ImageField(upload_to = 'profile/', default = 'profile/none/no-img.jpg')
	tel = models.CharField(max_length=400, default=0)
	def __str__(self):
		return self.username


class Car(models.Model):
	timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)
	# brand = models.IntegerField(default=0,blank=True)
	brand= models.ForeignKey(Brand, on_delete = models.CASCADE, default=1,blank=True, related_name='%(class)s_requests_created')
	title = models.CharField(max_length=400, default=0)
	text = models.TextField(default=0, blank=True)
	price = models.IntegerField(default=0)
	currency = models.IntegerField(choices=LABEL_CHOICES, blank=True, default=1)
	city = models.IntegerField(choices=CITY_CHOICES, blank=True, default=1)

	profile= models.ForeignKey(DriverUser, on_delete = models.CASCADE, default=1,blank=True, related_name='%(class)s_requests_created')
	year = models.IntegerField(default=2000,blank=True)
	car_pic = models.ImageField(upload_to = '', default = 'none/no-img.jpg')
	car_pic2 = models.ImageField(upload_to = '', default = 'none/no-img.jpg')
	car_pic3 = models.ImageField(upload_to = '', default = 'none/no-img.jpg')

	class Meta:
		permissions = (
			('can_add', 'can_add_post'),
		)
	def __str__(self):
		return self.title