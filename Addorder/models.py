from django.db import models
from Addproduct.models import AddProduct
from CustomerID.models import Customer
from django.utils import timezone
from django.db import models
from django.utils import timezone
from .models import AddProduct, Customer

class AddOrder(models.Model):
    product = models.ForeignKey(AddProduct, on_delete=models.CASCADE)
    order_no = models.CharField(max_length=100, unique=True)
    order_date = models.DateField(default=timezone.now) 
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.order_no
