from django.db import models
from Addcategory.models import AddCategory

class AddProduct(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(AddCategory, on_delete=models.CASCADE)
    description = models.TextField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

