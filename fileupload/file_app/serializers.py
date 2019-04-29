from rest_framework.serializers import (
     ModelSerializer,
)

from file_app.models import MyImage


class imageSerializer(ModelSerializer):

    class Meta:
        model = MyImage
        fields = ['created', 'place', 'model_pic', 'size']
        read_only_fields = ('pk', 'created', 'size')

    def validate(self, validated_data):
        validated_data['size'] = validated_data['model_pic'].size
        return validated_data

    def create(self, validated_data):
        return MyImage.objects.create(**validated_data)
