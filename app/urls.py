from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'units', views.UnitOfMeasureViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'services', views.ServiceViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'order-details', views.OrderDetailsViewSet)
router.register(r'image-organs', views.ImageOrganViewSet)
router.register(r'creaters', views.CreaterViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'organizations', views.OrganationViewSet)
router.register(r'vacancies', views.VakansiyaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
