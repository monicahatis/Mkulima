from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.conf import settings


# Create your models here.4
class AccountType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="pics", default="default.jpg")
    accountType = models.ForeignKey(
        AccountType, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.user.username + "'s profile"
