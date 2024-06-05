from django import forms
from .models import AddOrder

class AddOrderForm(forms.ModelForm):
    class Meta:
        model = AddOrder
        fields = ['product', 'order_no', 'order_date', 'CustomerID', 'expiry_date', 'quantity']
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None or quantity <= 0:
            raise forms.ValidationError('Quantity must be greater than zero.')
        return quantity