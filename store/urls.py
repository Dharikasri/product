"""productmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from CustomerID.views import login_view ,dashboard_view  
urlpatterns = [
    path('', login_view, name='root'),
    path('dashboard/',dashboard_view, name='dashboard'),
    path('admin/', admin.site.urls),
    path('order/', include('Addorder.urls')),
    path('Cate/', include('Addcategory.urls')),
    path('addproduct/', include('Addproduct.urls')),  
    path('CustomerID/', include('CustomerID.urls', namespace='CustomerID_app')),
    path('api1/', include('Addcategory.urls')),
]


