from restreklama import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
	path('add/car/', views.AddPostCar.as_view(), name='add-car'),
	path('add/item/', views.AddPostItem.as_view(), name='add-item'),


	# path('create/<id>/', views.CreateItemApiView.as_view(), name='item-create'),
	# url(r'^add/car/$', views.AddPostCar.as_view(), name='add-car'),
	# url(r'^add/item/$', views.AddPostItem.as_view(), name='add-item'),
	# url(r'^create/(?P<id>[\w-]+)/$', views.CreateItemApiView.as_view(), name='item-create'),


	url(r'^list/$', views.ListAPIView.as_view(), name='restcar-list'),
	url(r'^detail/(?P<id>[\w-]+)/$', views.DetailApiView.as_view(), name='detail'),
	url(r'^profile/list/$', views.ProfileListAPIView.as_view(), name='restcar-profile-list'),
	url(r'^edit/(?P<id>[\w-]+)/$', views.EditPost.as_view(), name='restcar-edit'),

]