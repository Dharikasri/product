from django.test import TestCase
from Addcategory.forms import AddCategoryForm

class AddCategoryFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Test Category',
            'parent': None  # or provide the parent category if required
        }
        form = AddCategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        invalid_form_data = {
            'name': '',  # Empty name field to make it invalid
            'parent': None
        }
        form = AddCategoryForm(data=invalid_form_data)
        self.assertFalse(form.is_valid())
