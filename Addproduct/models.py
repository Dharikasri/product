from django.db import models
from Addcategory.models import AddCategory
from decimal import Decimal


class AddProduct(models.Model):
    product_id = models.IntegerField(unique=True,default=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(AddCategory, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    expiry_date = models.DateField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name
