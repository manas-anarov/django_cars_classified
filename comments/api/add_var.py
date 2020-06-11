from comments.models import Comment
from django.conf import settings
from cars.models import DriverUser


user = DriverUser.objects.get(id=1)

user = DriverUser.objects.get(id=1)
model_type = self.request.GET.get("type")