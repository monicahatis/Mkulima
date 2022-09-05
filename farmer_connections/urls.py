from django.urls import path
from .views import Farmer_WH_Owner_Connection_View, Farmer_Buyer_Connection_View


urlpatterns = [
    path('farmer-wh-owner/', Farmer_WH_Owner_Connection_View, name="Farmer_WH_Owner_Connection"),
    path('farmer-buyer/', Farmer_Buyer_Connection_View, name="Farmer_Buyer_Connection")
]