# test_forms.py
from django.test import TestCase
from CustomerID.forms import CustomerForm

class CustomerFormTest(TestCase):
    def test_invalid_form(self):
        data = {
            'name': 'John Doe',
            'address': '123 Main St',
            'created_at': '2024-06-03'
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())
        

        print("Errors:", form.errors)
        print("Errors for 'mobile':", form.errors.get('mobile'))
