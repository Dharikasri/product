from django.urls import path
from .views import create_customer
from .views import customer_list

urlpatterns = [
    path('create/', create_customer, name='create_customer'),
    path('list/', customer_list, name='customer_list'), 
]