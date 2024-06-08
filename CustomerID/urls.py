from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CustomerID.views import CustomerListAPIView, login_view,product_list,logout_view
from CustomerID.views import order_list,accounts_view
from CustomerID.views import homepage_view
from Addorder.views import add_order_view


from . import views

app_name = 'CustomerID'

router = DefaultRouter()
router.register(r'customers', CustomerListAPIView, basename='customer')

urlpatterns = [
    path('login/',login_view, name='login_view'), 
    path('dashboard/',views.dashboard_view, name='dashboard'), 
    path('orders/',order_list, name='order_list'),
    path('add/<int:product_id>/', add_order_view, name='add_order'),
    path('products1/', product_list, name='product_list'),
    path('logout/', logout_view, name='logout'),
    path('', views.customer_list, name='customer_list'),  
    path('create/', views.customer_create, name='customer_create'), 
    path('customers/<int:pk>/update/', views.customer_update, name='customer_update'),  
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'), 
    path('api/', include(router.urls)), 
    path('accounts/', accounts_view, name='accounts'),
    path('home/',homepage_view, name='homepage'),
    
    

]

