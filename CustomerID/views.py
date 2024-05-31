

from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list') 
    else:
        form = CustomerForm()
    return render(request, 'create_customer.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})
