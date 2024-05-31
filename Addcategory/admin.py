from django.contrib import admin
from .models import AddCategory

class AddCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_filter = ['parent']
    search_fields = ['name']

admin.site.register(AddCategory, AddCategoryAdmin)

