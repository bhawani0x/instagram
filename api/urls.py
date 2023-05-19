from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'data/photo', views.PhotoViews),
router.register(r'data/category', views.CategoryViews),
router.register(r'data/tag', views.TagViews),

urlpatterns = [
    path('category/', views.CategoryViews.as_view({'get': 'list'}), name='category'),
    path('photo/', views.PhotoViews.as_view({'get': 'list'}), name='photo'),
    path('tag/', views.TagViews.as_view({'get': 'list'}), name='tag'),
]
urlpatterns += router.urls
