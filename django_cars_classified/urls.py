from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from cars import views as cars_views
from django.conf.urls.static import static
from django.conf import settings


from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('cars.urls', 'car'), namespace='car')),
    url(r'^reklama/', include('django_classified.urls', namespace='django_classified')),
	url(r'^api/v1/comments/', include(("comments.api.urls", 'comments-api') , namespace='comments-api')),
	url(r'^api/v1/accounts/', include(('restaccounts.urls', 'restaccounts'), namespace='restaccounts')),
	url(r'^api/v1/profile/', include(('restprofile.urls', 'restprofile'), namespace='restprofile')),
	url(r'^api/v1/reklama/', include(('restreklama.urls', 'restreklama'), namespace='restreklama')),
	
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)