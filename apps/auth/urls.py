from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivateView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/activate/<str:token>', ActivateView.as_view(), name='auth_activate')
]
