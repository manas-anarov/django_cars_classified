from restcars import views
from django.conf.urls import url

urlpatterns = [
	url(r'^add/$', views.AddPost.as_view(), name='restcar-add'),
	url(r'^brand/list/$', views.BrandListAPIView.as_view(), name='restcar-list-brand'),
	url(r'^list/$', views.CarListAPIView.as_view(), name='restcar-list'),
	url(r'^(?P<id>[\w-]+)/$', views.ShowPost.as_view(), name='restcar-show'),
	url(r'^list/(?P<id>[\w-]+)/$', views.CategoryListAPIView.as_view(), name='restcar-mow'),
	url(r'^city/(?P<id>[\w-]+)/$', views.CityListAPIView.as_view(), name='city-restcar'),
]