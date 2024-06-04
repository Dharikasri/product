from django.test import TestCase
from django.contrib.auth.models import User
from CustomerID.models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.customer = Customer.objects.create(
            user=self.user,
            name="Test Customer",
            address="Test Address",
            mobile="1234567890"
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "Test Customer")
        self.assertEqual(self.customer.address, "Test Address")
        self.assertEqual(self.customer.mobile, "1234567890")
        self.assertTrue(self.customer.created_at)

    def test_customer_string_representation(self):
        self.assertEqual(str(self.customer), "Test Customer")
