from django.urls import path, include

urlpatterns = [
    path('/auth', include('apps.auth.urls')),
    path('/products', include('apps.product.urls')),
    path('/users', include('apps.user.urls')),
]
