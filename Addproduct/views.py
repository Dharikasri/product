from django.shortcuts import render
from .models import AddProduct

def product_list(request):
    products = AddProduct.objects.all()
    return render(request, 'Addproduct/product_list.html', {'products': products})
