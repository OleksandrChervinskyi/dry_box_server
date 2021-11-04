from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import serializers as s

from apps.profile_.models import ProfileModel
from apps.profile_.serializers import ProfileSerializer
from utils.email_utils import MailUtils
from utils.jwt_utils import JwtUtils

from .models import CustomUser

UserModel: CustomUser = get_user_model()


class UserSerializer(s.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        token = JwtUtils.create_activated_token(user)
        request = self.context.get('request')
        url = request.build_absolute_uri(reverse('auth_activate', args=(token,)))
        MailUtils.register_mail_sender(user.profile.name, user.email, url)
        return user
