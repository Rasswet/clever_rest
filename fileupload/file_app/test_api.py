'''
For detail run: python manage.py test --verbosity 2
'''

import os
import json
import tempfile
import io
from urllib.parse import urlparse
from PIL import Image
from django.test import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from file_app.models import MyImage


class UploadVideoTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        settings.MEDIA_ROOT = tempfile.mkdtemp()

    def tearDownTestData(self):
        MyImage.objects.all().delete()

    @staticmethod
    def _create_test_file():
        stream = io.BytesIO()
        image = Image.new('RGB', (350, 350), (150, 150, 50, 0))
        image.save(stream, format='jpeg')
        return stream.getvalue()

    def test_smoke(self):
        url = '/api/images/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_images(self):
        file = self._create_test_file()
        new_filename = 'file.jpg'
        uploaded_file = SimpleUploadedFile(new_filename, file, content_type="image/jpg")
        place_value = "someplace"
        data = {
            'place': json.dumps(place_value),
            'model_pic': uploaded_file,
        }
        quest_url = reverse('file_app:upload_images-list')
        response = self.client.post(quest_url, data, format='multipart')
        response = self.client.get(quest_url)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(MyImage.objects.count(), 1)
        self.assertEqual(str(MyImage.objects.get().place), '"{}"'.format(place_value))

    def test_upload_image(self):
        file = self._create_test_file()
        new_filename = 'file.jpg'
        file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
        uploaded_file = SimpleUploadedFile(new_filename, file, content_type="image/jpg")
        place_value = "someplace"
        data = {
            'place': json.dumps(place_value),
            'model_pic': uploaded_file,
        }
        quest_url = reverse('file_app:upload_images-list')
        response = self.client.post(quest_url, data, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertIn('created', response.data)
        self.assertTrue(urlparse(
            response.data['model_pic']).path.startswith(settings.MEDIA_URL))
        self.assertTrue(os.path.exists(file_path))
        self.assertEqual(MyImage.objects.count(), 1)
        self.assertEqual(str(MyImage.objects.get().place), '"{}"'.format(place_value))
