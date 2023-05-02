from rest_framework import serializers
from .models import *


class UnitOfMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasure
        fields = '__all__'
                                                                           

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'image')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Service
        fields = ('id', 'name', 'category', 'price', 'unit_of_measure', 'quantity', 'images')



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailsSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer()

    class Meta:
        model = OrderDetails
        fields = '__all__'


class ImageOrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOrgan
        fields = '__all__'


class CreaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creater
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    image = ImageOrganSerializer()
    creaters = CreaterSerializer()
    cantact = ContactSerializer()

    class Meta:
        model = Organation
        fields = '__all__'


class VakansiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vakansiya
        fields = '__all__'