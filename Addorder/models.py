from django.db import models

class AddOrder(models.Model):
    product = models.ForeignKey('AddProduct', on_delete=models.CASCADE)
    order_no = models.CharField(max_length=100, unique=True)
    order_date = models.DateField()
    CustomerID = models.ForeignKey('CustomerID', on_delete=models.CASCADE)

    def __str__(self):
        return self.order_no