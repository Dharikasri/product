from rest_framework import serializers
from .models import AddCategory

class AddCategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(many=True, queryset=AddCategory.objects.all())

    class Meta:
        model = AddCategory
        fields = ['id', 'name', 'parent', 'subcategories']
