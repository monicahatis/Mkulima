from django.db import models

# Create your models here.


class Subscription(models.Model):
    SubscriptionType = models.CharField(max_length=300, unique=True)
    NumberofDuration = models.IntegerField()
    TotalAmount = models.IntegerField()
    description = models.CharField(max_length=300)


class Payment(models.Model):
    User_id = models.IntegerField()
    Subscription_id = models.CharField(max_length=300)
    TotalAmount = models.IntegerField()
