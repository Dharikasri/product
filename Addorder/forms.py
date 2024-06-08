from django import forms
from .models import AddOrder
from datetime import datetime

class AddOrderForm(forms.ModelForm):
    class Meta:
        model = AddOrder
        fields = ['order_no', 'order_date', 'CustomerID', 'quantity', 'product']
        widgets = {
            'order_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is None or quantity <= 0:
            raise forms.ValidationError('Quantity must be greater than zero.')
        return quantity
    
    def clean_order_date(self):
        order_date = self.cleaned_data.get('order_date')
        if not order_date:
            raise forms.ValidationError('This field is required.')
        return order_date

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Check if the instance is being created (not updated)
            self.initial['order_date'] = datetime.now().date()  # Set initial value to current date
