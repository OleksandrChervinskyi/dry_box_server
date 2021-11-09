from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.product.models import ProductModel
from apps.product.serializers import ProductSerializers
from paginations.my_pagination import MyPagination


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='Список товарів'))
@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='Створення нового товару'))
class ProductListCreateView(ListCreateAPIView):
    """
        get:
            Виводить список всі товарів
        post:
            Створення нового товару
    """
    serializer_class = ProductSerializers
    queryset = ProductModel.objects.all()
    pagination_class = MyPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'price')


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='Отримати товар'))
@method_decorator(name='put', decorator=swagger_auto_schema(operation_id='Оновити товар'))
@method_decorator(name='patch', decorator=swagger_auto_schema(operation_id='Оновити товар частково'))
@method_decorator(name='delete', decorator=swagger_auto_schema(operation_id='Видалити товар'))
class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
            get:
                Виводить товар
            put:
                Оновлює товар
            patch:
                Оновлює товар частково
            delete:
                Видаляє товар
    """
    serializer_class = ProductSerializers
    queryset = ProductModel.objects.all()
