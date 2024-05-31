from django.shortcuts import render
from .models import AddOrder

def order_list(request):
    orders = AddOrder.objects.all()
    return render(request, 'Addorder/order_list.html', {'orders': orders})

