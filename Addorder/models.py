from django.db import models
from Addproduct.models import AddProduct
from CustomerID.models import Customer

class AddOrder(models.Model):
    product = models.ForeignKey(AddProduct, on_delete=models.CASCADE)
    order_no = models.CharField(max_length=100, unique=True)
    order_date = models.DateField()
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expiry_date = models.DateField(null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.order_no
