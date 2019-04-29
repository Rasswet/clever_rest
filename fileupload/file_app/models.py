from django.db import models


class MyImage(models.Model):
    model_pic = models.ImageField(max_length=10000)
    place = models.CharField(max_length=20,  blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки в базу')
    size = models.IntegerField(default=0)

    def __str__(self):
        return '{} upload at {}'.format(self.place, self.created)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
