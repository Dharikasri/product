from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import AddProduct
from .forms import AddProductForm
from .serializers import AddProductSerializer

# View for listing products
def product_list(request):
    products = AddProduct.objects.all()
    return render(request, 'Addproduct/product_list.html', {'products': products})

# View for adding a new product
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list') 
    else:
        form = AddProductForm()
    return render(request, 'Addproduct/add_product.html', {'form': form})

# Viewset for REST API endpoints
class AddProductViewSet(viewsets.ModelViewSet):
    queryset = AddProduct.objects.all()
    serializer_class = AddProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
