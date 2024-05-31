from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('create-customer/', views.customer_create, name='create_customer'),
    path('customer/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
]
