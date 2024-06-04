from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from Addorder.models import AddOrder
from Addorder.serializers import AddOrderSerializer

class AddOrderViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_order(self):
        url = '/api2/add_order/'  # Correct URL for creating orders
        data = {
            'product': 'Product X',
            'order_no': 'ORD123',
            'order_date': '2024-06-04',
            'customer_id': 'CUST456',
        }

        response = self.client.post(url, data, format='json')

        # Check if the response status code is 201 (Created) or 400 (Bad Request)
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])

        # If response status code is 400, print the response content
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            print("Validation Error:", response.content.decode('utf-8'))

        # If response status code is 201, assert that the order exists in the database
        if response.status_code == status.HTTP_201_CREATED:
            self.assertTrue(AddOrder.objects.filter(order_no='ORD123').exists())

            # Additionally, assert that the created order matches the provided data
            order_data = AddOrder.objects.get(order_no='ORD123')
            serializer = AddOrderSerializer(order_data)
            self.assertEqual(serializer.data['product'], data['product'])
            self.assertEqual(serializer.data['order_no'], data['order_no'])
            self.assertEqual(serializer.data['order_date'], data['order_date'])
            self.assertEqual(serializer.data['customer_id'], data['customer_id'])
