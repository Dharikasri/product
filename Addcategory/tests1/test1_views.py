from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from Addcategory.models import AddCategory
from Addcategory.forms import AddCategoryForm

class CreateCategoryTestCase(TestCase):
    def setUp(self):
        self.url = reverse('create_category')
        self.valid_data = {
            'name': 'Test Category',
            # Include any other required fields here
        }

    def test_create_category_view_with_valid_data(self):
        """
        Test create_category view with valid form data
        """
        response = self.client.post(self.url, self.valid_data)
        
        # Check that the response status code is 302 Found (redirect)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        
        # Check that a new category is created in the database
        self.assertTrue(AddCategory.objects.filter(name='Test Category').exists())

    def test_create_category_view_with_invalid_data(self):
        """
        Test create_category view with invalid form data
        """
        invalid_data = {
            'name': ''  # Empty name field to make it invalid
        }
        response = self.client.post(self.url, invalid_data)
        
        # Check that the response status code is 200 OK (form is not valid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that a new category is not created in the database
        self.assertFalse(AddCategory.objects.filter(name='').exists())
