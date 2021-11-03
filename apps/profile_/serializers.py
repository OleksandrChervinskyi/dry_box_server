from rest_framework import serializers as s
from .models import ProfileModel


class ProfileSerializer(s.ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ('user',)


class ProfileAvatarSerializer(s.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)
        extra_kwargs = {
            'avatar': {'required': True}
        }
