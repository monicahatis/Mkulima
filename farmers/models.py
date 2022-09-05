from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Farmers(models.Model):
    produce = models.CharField(max_length=100)
    Price_per_kilo = models.IntegerField()
    Location = models.CharField(max_length=100)
    Contacts = models.IntegerField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='farmers')
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="pics")

    def get_absolute_url(self):
        return reverse("farmers:details-farmers", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-published']  # ensure what is published latest come first

    def __str__(self):
        return self.produce
