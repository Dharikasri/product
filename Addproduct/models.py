from django.db import models

class AddProduct(models.Model):
    name = models.CharField(max_length=100)
    Category = models.ForeignKey('AddCategory', on_delete=models.CASCADE)
    description = models.TextField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name