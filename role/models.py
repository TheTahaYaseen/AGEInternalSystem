from django.db import models

# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=255, unique=True)
    access_to_shop_management = models.BooleanField()
    access_to_factory_management = models.BooleanField()