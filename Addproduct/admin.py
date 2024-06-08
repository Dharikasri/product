from django.contrib import admin
from .models import AddProduct

class AddProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','description','expiry_date','price','product_id') 
    
admin.site.register(AddProduct, AddProductAdmin)

