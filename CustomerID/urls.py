from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CustomerID.views import CustomerListAPIView, login_view,product_list

from . import views

app_name = 'CustomerID'

router = DefaultRouter()
router.register(r'customers', CustomerListAPIView, basename='customer')

urlpatterns = [
    path('login/',login_view, name='login_view'), 
    path('dashboard/', views.dashboard_view, name='dashboard'), 
    path('products1/', product_list, name='product_list'),
    path('', views.customer_list, name='customer_list'),  
    path('create/', views.customer_create, name='customer_create'), 
    path('customers/<int:pk>/update/', views.customer_update, name='customer_update'),  
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'), 
    path('api/', include(router.urls)), 

]

