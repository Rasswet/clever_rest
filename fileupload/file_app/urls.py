from django.conf.urls import include, url
from file_app.views import UploadImageViewSet
from rest_framework.routers import DefaultRouter

app_name = "file_app"

router = DefaultRouter()
router.register('images', UploadImageViewSet, basename='upload_images')

urlpatterns = [
    url(r'^', include(router.urls), name='root_upload_images'),
]
