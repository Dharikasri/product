from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddCategoryViewSet

router = DefaultRouter()
router.register(r'categories', AddCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
