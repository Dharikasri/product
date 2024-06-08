from django.contrib import admin
from .models import AddOrder

class AddOrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'order_date', 'product', 'CustomerID','product_id')
    list_filter = ('order_date', 'product')
    search_fields = ('order_no', 'CustomerID__name') 

admin.site.register(AddOrder, AddOrderAdmin)



