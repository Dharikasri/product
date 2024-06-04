from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from Addproduct.models import AddProduct

class AddProductViewSetTestCase(APITestCase):
    def setUp(self):
        self.create_url = reverse('addproduct-list') 
        self.valid_payload = {'name': 'Test Product', 'description': 'Test Description'}

    def test_create_product(self):
        initial_count = AddProduct.objects.count()
        response = self.client.post(self.create_url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AddProduct.objects.count(), initial_count + 1)

        created_product = AddProduct.objects.latest('id')
        self.assertEqual(created_product.name, self.valid_payload['name'])
        self.assertEqual(created_product.description, self.valid_payload['description'])
