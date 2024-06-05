from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import product_list, AddProductViewSet,add_product

router = DefaultRouter()
router.register(r'products', AddProductViewSet)

urlpatterns = [
    path('api3/', include(router.urls)),
    path('products1/', product_list, name='product_list'),
    path('prod/',add_product, name='add_product'),
]
