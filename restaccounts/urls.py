from restaccounts import views
from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken import views as authviews

urlpatterns = [
	url(r'^register/$', views.Register.as_view(), name='register'),
	url(r'^profile/$', views.Profile.as_view(), name='profile'),
	url(r'^edit/$', views.MyProfileAPIView.as_view(), name='edit'),
	path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),
]

#curl -X POST -d "username=samuray&password=q11111111" http://192.168.8.100:8000/

#curl -H "Authorization: Token 14cb31d9c5d609fde7759fdbc3b2aa905ce336c4" http://192.168.8.100:8000/api/v1/profile/list/
