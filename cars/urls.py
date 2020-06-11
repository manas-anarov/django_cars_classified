from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	# url(r'^add', views.add, name='add'),
	path('add/', views.CarCreateView.as_view(), name='add'),

	# url(r'^', views.all_posts, name='list'),

	# path('',views.all_posts, name='list'),
	path('', views.CarListView.as_view(), name='list'),

	url(r'^(?P<pk>\d+)/$', views.CarDetailView.as_view(), name='post-show'),

	url(r'^category/(?P<pk>\d+)/$', views.list_category, name='category'),
]