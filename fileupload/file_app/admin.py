from django.contrib import admin
from file_app.models import MyImage


class MyImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'created')
    list_filter = ('created',)


admin.site.register(MyImage, MyImageAdmin)
