from django.test import TestCase, Client
from django.urls import reverse
from CustomerID.models import Customer

class CustomerViewsTestCase(TestCase):
    def setUp(self):
        # Create a Customer object for testing
        self.customer = Customer.objects.create(name='Test Customer', mobile='1234567890', address='Test Address')

    def test_customer_update_view(self):
        # Use the created customer's pk for testing
        url = reverse('CustomerID:customer_update', kwargs={'pk': self.customer.pk})
        response = self.client.post(url, {'mobile': '9876543210', 'name': 'Updated Name', 'address': 'Updated Address'})
        self.assertEqual(response.status_code, 302)  # Assuming successful redirect
        # Add more assertions as needed for this test case

    def test_customer_delete_view(self):
        url = reverse('CustomerID:customer_delete', kwargs={'pk': self.customer.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Assuming successful redirect
        # Add more assertions as needed for this test case
