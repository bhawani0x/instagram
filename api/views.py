from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import *


class CategoryViews(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = CategoryViewsSerializer
    queryset = Category.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['tag_name']


class TagViews(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = TagViewsSerializer
    queryset = Tag.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name']


class PhotoViews(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PhotoViewsSerializer
    queryset = Photo.objects.all().order_by('id')
