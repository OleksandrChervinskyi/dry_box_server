from rest_framework import serializers as s

from .models import ProductModel


class ProductSerializers(s.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
