
from rest_framework import generics, viewsets
from .models import AddCategory
from .serializers import AddCategorySerializer
from django.shortcuts import render, redirect
from .models import AddCategory
from .forms import AddCategoryForm

def category_list(request):
    categories = AddCategory.objects.all()
    return render(request, 'Addcategory/category_list.html', {'categories': categories})

def create_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to the category list page after creating a new category
    else:
        form = AddCategoryForm()
    return render(request, 'Addcategory/create_category.html', {'form': form})


class AddCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = AddCategory.objects.all()
    serializer_class = AddCategorySerializer

class AddCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddCategory.objects.all()
    serializer_class = AddCategorySerializer

class AddCategoryViewSet(viewsets.ModelViewSet):
    queryset = AddCategory.objects.all()
    serializer_class = AddCategorySerializer

