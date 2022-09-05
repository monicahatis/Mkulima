from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Warehouses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    warehousename = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    storagefee = models.IntegerField()
    capacity = models.IntegerField()
    description = models.TextField(max_length=100)
    contacts = models.IntegerField()
    image = models.ImageField(upload_to="pics")
    uploaded_at = models.DateTimeField(default=timezone.now)
