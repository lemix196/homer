from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=150, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    product_quantity = models.IntegerField() # add validator for negative values
