from django.shortcuts import render
from .models import AddCategory

def category_list(request):
    categories = AddCategory.objects.all()
    return render(request, 'Addcategory/category_list.html', {'categories': categories})

