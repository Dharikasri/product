from rest_framework import serializers
from .models import AddCategory

class AddCategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(many=True, queryset=AddCategory.objects.all(), required=False)

    class Meta:
        model = AddCategory
        fields = ['id', 'name', 'parent', 'subcategories']
