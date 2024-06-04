from django.test import TestCase
from datetime import date
from Addproduct.models import AddProduct
from Addcategory.models import AddCategory

class AddProductModelTestCase(TestCase):
    def setUp(self):
        category = AddCategory.objects.create(name='Test Category')
        self.product = AddProduct.objects.create(
            name='Test Product',
            category=category,
            description='Test Description',
            expiry_date=date.today(),
        )

    def test_product_creation(self):
        """Test AddProduct model creation"""
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.category.name, 'Test Category')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(self.product.expiry_date, date.today())
