from rest_framework import serializers
from .models import AddProduct

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddProduct
        fields = '__all__'
