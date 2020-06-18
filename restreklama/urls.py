from restreklama import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
	path('add/car/', views.CreateCar.as_view(), name='create-car'),
	path('add/item/', views.CreateItem.as_view(), name='create-item'),
	path('list/', views.ListAPIView.as_view(), name='list'),
	path('detail/<id>/', views.DetailApiView.as_view(), name='detail'),
	path('profile/list/', views.ProfileListAPIView.as_view(), name='profile-list'),
	path('edit/<id>/', views.EditPost.as_view(), name='edit'),
]