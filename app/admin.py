from django.contrib import admin
from .models import Service, Category, UnitOfMeasure, Image

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(UnitOfMeasure)
admin.site.register(Image)