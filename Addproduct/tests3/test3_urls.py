from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from Addproduct.models import AddProduct


class ProductCreationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('addproduct-list')  
        self.valid_payload = {'name': 'New Product', 'description': 'New Description'}

    def test_product_creation(self):
        """Test product creation through API"""
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AddProduct.objects.count(), 1)  

        created_product = AddProduct.objects.first()
        self.assertEqual(created_product.name, self.valid_payload['name'])
        self.assertEqual(created_product.description, self.valid_payload['description'])
    
