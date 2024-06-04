from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddCategoryViewSet
from . import views

router = DefaultRouter()
router.register(r'categories', AddCategoryViewSet)

urlpatterns = [
    path('category/list/', views.category_list, name='category_list'),
    path('category/create/', views.create_category, name='create_category'),
    path('api1/', include(router.urls)),
]
