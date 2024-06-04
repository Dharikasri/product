from django import forms
from .models import AddCategory

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = AddCategory
        fields = ['name', 'parent']
