from django.contrib import admin
from .models import AddProduct

class AddProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','description','expiry_date') 
    
admin.site.register(AddProduct, AddProductAdmin)

