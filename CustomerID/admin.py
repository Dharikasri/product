from django.contrib import admin
from CustomerID.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display=('user','name','address','created_at')

admin.site.register(Customer, CustomerAdmin)
