from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path(r'', views.hello, name='hello'),
    path('admin/', admin.site.urls),
    url(r'^api/', include('file_app.urls', namespace='api')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
