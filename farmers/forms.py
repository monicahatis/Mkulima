from django import forms
from django.forms import fields
from .models import Farmers

class PostForm(forms.ModelForm):
    class Meta:
        model = Farmers
        fields= "__all__"