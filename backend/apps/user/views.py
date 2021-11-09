from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny

from apps.profile_.serializers import ProfileAvatarSerializer
from .models import CustomUser
from .serializers import UserSerializer

UserModel: CustomUser = get_user_model()


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='Список товарів'))
@method_decorator(name='post', decorator=swagger_auto_schema(operation_id='Створення нового товару'))
class UserListCreateView(ListCreateAPIView):
    """
        get:
            Виводить список всі користувачів
        post:
            Створення нового користувача
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_serializer_context(self):
        return {"request": self.request}


@method_decorator(name='put', decorator=swagger_auto_schema(operation_id='Додати аватар для користувача'))
class UserAddAvatarView(GenericAPIView, UpdateModelMixin):
    """
        put:
            Додає аватар до користувача
    """
    serializer_class = ProfileAvatarSerializer

    def get_object(self):
        return self.request.user.profile

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)
