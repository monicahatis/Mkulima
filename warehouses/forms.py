from django import forms
from .models import Warehouses
from farmer_connections.models import Farmer_WH_Owner_Connection


class WarehouseCreationForm(forms.ModelForm):
    class Meta:
        model = Warehouses
        fields = ['warehousename', 'location', 'storagefee',
                  'capacity', 'description', 'contacts', 'image']


class WarehouseUpdateForm(forms.ModelForm):
    class Meta:
        model = Warehouses
        fields = ['warehousename', 'location', 'storagefee',
                  'capacity', 'description', 'contacts', 'image']

class CommunicationsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wh_owner_id'].widget.attrs['readonly'] = "readonly"
    class Meta:
        model = Farmer_WH_Owner_Connection
        fields = ['wh_owner_id','wh_store_number', 'message', 'farmer_id']