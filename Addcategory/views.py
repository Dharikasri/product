
from rest_framework import generics, viewsets
from .models import AddCategory
from .serializers import AddCategorySerializer

class AddCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = AddCategory.objects.all()
    serializer_class = AddCategorySerializer

class AddCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddCategory.objects.all()
    serializer_class = AddCategorySerializer

class AddCategoryViewSet(viewsets.ModelViewSet):
    queryset = AddCategory.objects.all()
    serializer_class = AddCategorySerializer

