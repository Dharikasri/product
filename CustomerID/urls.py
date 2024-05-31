from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerListAPIView, CustomerDetailAPIView

router = DefaultRouter()
router.register(r'customers', CustomerListAPIView, basename='customer-list')

urlpatterns = [
    path('', include(router.urls)),
    path('customer-detail/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
]
