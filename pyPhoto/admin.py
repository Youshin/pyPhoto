from django.contrib import admin
from .models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'image_file', 'filtered_image_file']

admin.site.register(Photo)