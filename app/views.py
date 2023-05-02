from rest_framework import viewsets
from .models import UnitOfMeasure, Image, Category, Service, Client, Order, OrderDetails, ImageOrgan, Creater, Contact, Organation, Vakansiya
from .serializers import UnitOfMeasureSerializer, ImageSerializer, CategorySerializer, ServiceSerializer, ClientSerializer, OrderSerializer, OrderDetailsSerializer, ImageOrganSerializer, CreaterSerializer, ContactSerializer, OrganizationSerializer, VakansiyaSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status





class UnitOfMeasureViewSet(viewsets.ModelViewSet):
    queryset = UnitOfMeasure.objects.all()
    serializer_class = UnitOfMeasureSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def create(self, request, *args, **kwargs):
        images_data = request.data.pop('images', None)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if images_data:
            images = []
            for image_data in images_data:
                image = Image.objects.create(
                    name=image_data.get('name', ''),
                    image=image_data.get('image', None),
                )
                images.append(image)
            serializer.instance.images.set(images)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        images_data = request.data.pop('images', None)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if images_data is not None:
            images = []
            for image_data in images_data:
                image_id = image_data.get('id', None)
                if image_id is not None:
                    try:
                        image = Image.objects.get(id=image_id)
                        image.name = image_data.get('name', image.name)
                        image.image = image_data.get('image', image.image)
                        image.save()
                        images.append(image)
                    except Image.DoesNotExist:
                        pass
                else:
                    image = Image.objects.create(
                        name=image_data.get('name', ''),
                        image=image_data.get('image', None),
                    )
                    images.append(image)
            instance.images.set(images)
        return Response(serializer.data)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer

class ImageOrganViewSet(viewsets.ModelViewSet):
    queryset = ImageOrgan.objects.all()
    serializer_class = ImageOrganSerializer

class CreaterViewSet(viewsets.ModelViewSet):
    queryset = Creater.objects.all()
    serializer_class = CreaterSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class OrganationViewSet(viewsets.ModelViewSet):
    queryset = Organation.objects.all()
    serializer_class = OrganizationSerializer

class VakansiyaViewSet(viewsets.ModelViewSet):
    queryset = Vakansiya.objects.all()
    serializer_class = VakansiyaSerializer
