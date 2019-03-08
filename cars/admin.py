from django.contrib import admin
from cars.models import Car
from cars.models import Brand


admin.site.register(Car)
admin.site.register(Brand)