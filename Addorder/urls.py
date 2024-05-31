from django.urls import path, include
from .views import order_list, AddOrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'add_order', AddOrderViewSet)

urlpatterns = [
    path('orders/', order_list, name='order-list'), 
    path('', include(router.urls)), 
]
