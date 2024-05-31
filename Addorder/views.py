from django.urls import path
from django.shortcuts import render
from rest_framework import viewsets
from .models import AddOrder
from .serializers import AddOrderSerializer


def order_list(request):
    orders = AddOrder.objects.all()
    return render(request, 'Addorder/order_list.html', {'orders': orders})

class AddOrderViewSet(viewsets.ModelViewSet):
    queryset = AddOrder.objects.all()
    serializer_class = AddOrderSerializer

