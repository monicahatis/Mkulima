from rest_framework import serializers
from .models import Farmer_WH_Owner_Connection, Farmer_Buyer_Connection


class FarmerConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer_WH_Owner_Connection # this is the model that is being serialized
        fields = ('farmer_id', 'wh_owner_id','wh_store_number', 'message')

class FarmerBuyerConnectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer_Buyer_Connection # this is the model that is being serialized
        fields = ('farmer_id', 'buyer_id', 'created_date', 'product_id', 'message', 'status')