from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.product.models import ProductModel
from apps.product.serializers import ProductSerializers
from paginations.my_pagination import MyPagination


# Create your views here.

class ProductListCreateView(ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = ProductModel.objects.all()
    pagination_class = MyPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'price')


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializers
    queryset = ProductModel.objects.all()
