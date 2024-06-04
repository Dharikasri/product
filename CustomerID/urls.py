from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerListAPIView, product_list
from . import views

app_name = 'CustomerID'

router = DefaultRouter()
router.register(r'customers', CustomerListAPIView, basename='customer')


urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('create/', views.customer_create, name='customer_create'),
    path('<int:pk>/update/', views.customer_update, name='customer_update'),
    path('<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('api4/', include(router.urls)),
    path('products1/', product_list, name='product_list'),

]

