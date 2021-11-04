from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny

from apps.profile_.serializers import ProfileAvatarSerializer
from .models import CustomUser
from .serializers import UserSerializer

UserModel: CustomUser = get_user_model()


class UserListCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_serializer_context(self):
        return {"request": self.request}


class UserAddAvatarView(GenericAPIView, UpdateModelMixin):
    serializer_class = ProfileAvatarSerializer

    def get_object(self):
        return self.request.user.profile

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)
