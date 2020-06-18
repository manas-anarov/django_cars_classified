from django.contrib import admin
from .models import  CarType
from django_classified.models import Image
from .models import  ThumbnailsImage

from .models import  ItemMy, ItemType, CategoryForCar

admin.site.register(CarType)
admin.site.register(Image)
admin.site.register(ThumbnailsImage)

admin.site.register(ItemMy)
admin.site.register(ItemType)
admin.site.register(CategoryForCar)