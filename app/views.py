from rest_framework import viewsets
from .models import Service, Image
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        images_data = self.request.FILES.getlist('images')
        service = serializer.save()

        for image_data in images_data:
            image = Image.objects.create(
                name=image_data.name,
                image=image_data,
            )
            service.images.add(image)
    


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
   

class UnitOfMeasureViewSet(viewsets.ModelViewSet):
    queryset = UnitOfMeasure.objects.all()
    serializer_class = UnitOfMeasureSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    

# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer