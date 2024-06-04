from django.shortcuts import render
from rest_framework import viewsets
from .models import AddProduct
from .serializers import AddProductSerializer
from .models import AddProduct
from rest_framework import viewsets, status
from rest_framework.response import Response 


def product_list(request):
    products = AddProduct.objects.all()
    return render(request, 'Addproduct/product_list.html', {'products': products})

class AddProductViewSet(viewsets.ModelViewSet):
    queryset = AddProduct.objects.all()
    serializer_class = AddProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
