from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile = models.CharField(max_length=15)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
