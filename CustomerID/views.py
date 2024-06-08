from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import viewsets
from .models import Customer
from .forms import CustomerForm
from .serializers import CustomerSerializer
from Addcategory.models import AddCategory
from Addproduct.models import AddProduct
from Addorder.models import AddOrder
from django.contrib import messages

# Views for managing customers
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
            return redirect(reverse('CustomerID:customer_list'))
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

# API view for customers
class CustomerListAPIView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Views for user authentication
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'Registration/login.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
from django.contrib import messages
from Addcategory.models import AddCategory
from Addproduct.models import AddProduct
from Addorder.models import AddOrder
from Addorder.forms import AddOrderForm

@login_required
def dashboard_view(request):
    categories = AddCategory.objects.all()
    products = AddProduct.objects.all()
    return render(request, 'Registration/dashboard.html', {'categories': categories, 'products': products})

def product_list(request):
    return render(request, 'Addproduct/product_list.html')


def logout_view(request):
    logout(request)
    return redirect('CustomerID:login_view')

def accounts_view(request):
    users_with_customers = User.objects.filter(customer__isnull=False)
    return render(request, 'Registration/accounts.html', {'users_with_customers': users_with_customers})

def homepage_view(request):
    return render(request, 'Registration/Homepage.html')


@login_required

@login_required
@login_required
def add_order_view(request):
    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            try:
                product = AddProduct.objects.get(id=product_id)
                # Prepopulate the form with product ID and quantity
                form = AddOrderForm(initial={'product_id': product_id, 'quantity': quantity})
                return render(request, 'Addorder/add_order.html', {'form': form})
            except AddProduct.DoesNotExist:
                form.add_error('product_id', 'Product with this ID does not exist')
    else:
        form = AddOrderForm()
    return render(request, 'Addorder/add_order.html', {'form': form})
@login_required
def order_list(request):
    orders = AddOrder.objects.all()
    return render(request, 'Addorder/order_list.html', {'orders': orders})