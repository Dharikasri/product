from django.shortcuts import render
from rest_framework import viewsets
from .models import AddOrder
from .serializers import AddOrderSerializer
from rest_framework.response import Response
from rest_framework import status

class AddOrderViewSet(viewsets.ModelViewSet):
    queryset = AddOrder.objects.all()
    serializer_class = AddOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def order_list(request):
    orders = AddOrder.objects.all()
    return render(request, 'Addorder/order_list.html', {'orders': orders})

from django.shortcuts import render, redirect
from .forms import AddOrderForm

def add_order_view(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = AddOrderForm()
    return render(request, 'Addorder/add_order.html', {'form': form})