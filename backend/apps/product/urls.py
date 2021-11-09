from django.urls import path

from backend.apps.product.views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product_list_create'),
    path('/<int:pk>', ProductRetrieveUpdateDestroyView.as_view(), name='product_retrieve_update_delete')
]