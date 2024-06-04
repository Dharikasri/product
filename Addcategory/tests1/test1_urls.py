
from django.test import TestCase
from Addcategory.models import AddCategory
from Addcategory.serializers import AddCategorySerializer

class AddCategorySerializerTestCase(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'Test Category',
            # Include any other required fields here
        }
        self.serializer = AddCategorySerializer(data=self.valid_data)

    def test_serializer_with_valid_data(self):
        """
        Test serializer with valid data
        """
        is_valid = self.serializer.is_valid()
        if not is_valid:
            print("Serializer errors:", self.serializer.errors)
        self.assertTrue(is_valid, f"Serializer is not valid. Errors: {self.serializer.errors}")
        if is_valid:
            self.serializer.save()
            self.assertTrue(AddCategory.objects.filter(name='Test Category').exists())

    def test_serializer_with_invalid_data(self):
        """
        Test serializer with invalid data
        """
        invalid_data = {'name': ''}  # Empty name field to make it invalid
        serializer = AddCategorySerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

    # Add more test cases as needed
