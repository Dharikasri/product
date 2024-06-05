from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from .models import Customer
from .forms import CustomerForm
from .serializers import CustomerSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from Addcategory.models import AddCategory 
from Addproduct.models import AddProduct
from Addorder.models import AddOrder



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

# API view for customers
class CustomerListAPIView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Views for user authentication
from django.contrib import messages

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


@login_required
def dashboard_view(request):
    categories = AddCategory.objects.all()
    products = AddProduct.objects.all()

    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        if category_id is None or product_id is None:
            messages.error(request, 'Please select both a category and a product.')
            return redirect('/dashboard/')

        print(f'Product ID: {product_id}, Quantity: {quantity}')
        print(f'Selected Category ID: {category_id}')
        print(f'Selected Product ID: {product_id}')

        
        return redirect('/add/')  # Replace 'add_order' with the actual URL name of the add_order page
    else:
        return render(request, 'Registration/dashboard.html', {'categories': categories, 'products': products})



def product_list(request):
    return render(request, 'Addproduct/product_list.html')

def order_list(request):
    return render(request, 'Addorder/order_list.html')

def logout_view(request):
    logout(request)
    return redirect('CustomerID:login_view')

def accounts_view(request):
    users_with_customers = User.objects.filter(customer__isnull=False)
    return render(request, 'Registration/accounts.html', {'users_with_customers': users_with_customers})

def homepage_view(request):
    return render(request, 'Registration/Homepage.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse

def add_product(request):
    return render(request, 'Addproduct/add_product.html')

def purchase_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        print(f'Product ID: {product_id}, Quantity: {quantity}')
        return HttpResponse('Purchase successful!')
    else:
        return HttpResponse('Method not allowed')
