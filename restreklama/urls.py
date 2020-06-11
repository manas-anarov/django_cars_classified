from restreklama import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
	path('add/car/', views.AddPostCar.as_view(), name='add-car'),
	path('add/item/', views.AddPostItem.as_view(), name='add-item'),
	path('list/', views.ListAPIView.as_view(), name='list'),
	path('detail/<id>/', views.DetailApiView.as_view(), name='detail'),
	path('profile/list/', views.ProfileListAPIView.as_view(), name='profile-list'),
	path('edit/<id>/', views.ProfileListAPIView.as_view(), name='edit'),
]