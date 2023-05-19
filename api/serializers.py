from rest_framework import serializers

from .models import *


class CategoryViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PhotoViewsSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    tag_name = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = '__all__'

    def get_category_name(self, obj):
        category_names = obj.post_category.all()
        return [category.category_name for category in category_names]

    def get_tag_name(self, obj):
        tag_names = obj.post_tag.all()
        return [tag.tag_name for tag in tag_names]
