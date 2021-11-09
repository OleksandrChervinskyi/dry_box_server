from django.db import models


# Create your models here.

class ProductModel(models.Model):
    class Meta:
        db_table = 'product'

    name = models.CharField(max_length=500)
    descriptions = models.CharField(max_length=2000)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

