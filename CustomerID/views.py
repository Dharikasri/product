from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from rest_framework import viewsets
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm
from .serializers import CustomerSerializer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'CustomerID/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'CustomerID/customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'CustomerID/customer_form.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'CustomerID/customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'CustomerID/customer_delete.html', {'customer': customer})

class CustomerListAPIView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'Registration/login.html') 
    return render(request, 'Registration/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'Registration/dashboard.html')
 

def product_list(request):
    return render(request, 'Addproduct/product_list.html')


def order_list(request):
     return render(request, 'Addorder/order_list.html')
 
def logout_view(request):
    logout(request)
    return redirect('CustomerID:login_view')

@login_required
def dashboard(request):
    return render(request, 'Registration/dashboard.html')

from django.contrib.auth.models import User

def accounts_view(request):
    users = User.objects.all()
    return render(request, 'Registration/accounts.html', {'users': users})
