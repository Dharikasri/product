from django.urls import path, include
from .views import AddOrderViewSet, order_list
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'add_order', AddOrderViewSet)


urlpatterns = [
    path('api2/', include(router.urls)),
    path('orders/', order_list, name='order-list'),
]
