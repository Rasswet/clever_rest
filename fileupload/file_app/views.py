from rest_framework import viewsets
from file_app.serializers import imageSerializer
from file_app.models import MyImage
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend


class UploadImageViewSet(viewsets.ModelViewSet):
    serializer_class = imageSerializer
    queryset = MyImage.objects.all()

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('created', 'size')
