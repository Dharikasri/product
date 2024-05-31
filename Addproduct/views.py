from django.shortcuts import render
from rest_framework import viewsets
from .models import AddProduct
from .serializers import AddProductSerializer
from .models import AddProduct

def product_list(request):
    products = AddProduct.objects.all()
    return render(request, 'Addproduct/product_list.html', {'products': products})

class AddProductViewSet(viewsets.ModelViewSet):
    queryset = AddProduct.objects.all()
    serializer_class = AddProductSerializer
