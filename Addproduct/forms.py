# forms.py
from django import forms
from .models import AddProduct

class AddProductForm(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = ['product_id', 'name', 'category', 'description', 'expiry_date', 'price']
