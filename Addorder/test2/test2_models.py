from django.test import TestCase
from datetime import date
from Addorder.models import AddOrder
from Addproduct.models import AddProduct
from CustomerID.models import Customer

class AddOrderTestCase(TestCase):
    def setUp(self):
        # Create sample AddProduct instance
        self.product = AddProduct.objects.create(name='Test Product')

        # Create sample Customer instance
        self.customer = Customer.objects.create(name='Test Customer')

    def test_create_order(self):
        # Create an AddOrder instance
        order = AddOrder.objects.create(
            product=self.product,
            order_no='12345',
            order_date=date.today(),
            CustomerID=self.customer
        )
        
        # Print out the order object for debugging
        print(order)
        
        # Check if the order was created successfully
        self.assertIsNotNone(order.id)
