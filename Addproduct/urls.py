from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import product_list, AddProductViewSet

urlpatterns = [
    path('products/', product_list, name='product_list'),
]

router = DefaultRouter()
router.register(r'products', AddProductViewSet)

urlpatterns += [
    path('', include(router.urls)),
]
