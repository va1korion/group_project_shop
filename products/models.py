from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=255, blank=False)
    price = models.DecimalField(default=300, decimal_places=2, max_digits=100, blank=False)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
