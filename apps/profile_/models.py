from django.db import models

from django.contrib.auth import get_user_model
from utils.file_utils import FileUtils

UserModel = get_user_model()


# Create your models here.
class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    born = models.DateField()
    avatar = models.ImageField(upload_to=FileUtils.avatar_upload_to, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
