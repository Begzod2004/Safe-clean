from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ServiceViewSet, UnitOfMeasureViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'unit_of_measures', UnitOfMeasureViewSet, basename='unit_of_measures')
router.register(r'images', ImageViewSet, basename='images')

urlpatterns = [
    path('', include(router.urls)),
]