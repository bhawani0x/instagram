from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["photo_name", "insta_post"]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
