from django.db import models

class Car(models.Model):
	timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)
	brand = models.IntegerField(default=0)
	title = models.CharField(max_length=400, default=0)
	text = models.CharField(max_length=400, default=0)
	price = models.IntegerField(default=0)
	def __str__(self):
		return self.title
