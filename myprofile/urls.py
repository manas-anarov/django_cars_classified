from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^add', views.add, name='add'),
	# url(r'^list', views.list_author, name='list'),
	url(r'^list', views.ProfileListView.as_view(), name='list'),

	# url(r'^delete/(?P<pk>\d+)/$', views.delete_post, name='delete'),
	url(r'^delete/(?P<pk>\d+)/$', views.delete_post, name='delete'),
	# url(r'^update/(?P<pk>\d+)/$', views.update_post, name='update'),
	url(r'^update/(?P<pk>\d+)/$', views.ProfileUpdateView.as_view(), name='update'),
	# url(r'^category/(?P<pk>\d+)/$', views.list_category, name='category'),
]