from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Farmer_WH_Owner_Connection(models.Model):
    farmer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farmer')
    wh_owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wh_owner')
    created_date = models.DateTimeField(auto_now_add=True)
    wh_store_number = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=2, default="1")
   
    def __str__(self):
       return self.farmer_id

class Farmer_Buyer_Connection(models.Model):
    farmer_id = models.CharField(max_length=20)
    buyer_id = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    product_id = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
   
    def __str__(self):
       return self.farmer_id
