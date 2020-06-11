from django.contrib import admin
from cars.models import Car
from cars.models import Brand
from cars.models import DriverUser

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(DriverUser)