from django.urls import path, include
from .views import AddOrderViewSet, order_list,add_order_view
from rest_framework.routers import DefaultRouter

appname= 'Addorder' 

router = DefaultRouter()
router.register(r'add_order', AddOrderViewSet)


urlpatterns = [
    path('api2/', include(router.urls)),
    path('orders/', order_list, name='order_list'),
    path('add/', add_order_view, name='add_order'),
]
