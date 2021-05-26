from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=255, blank=False)
    price = models.DecimalField(default=300, decimal_places=2, max_digits=100, blank=False)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, default='media/itmo_tagline.png', upload_to='products/')
    category = models.TextField(null=True)
    quantity = models.IntegerField(default=0, null=False)

    def get_absolute_url(self):
        return reverse("Product", kwargs={"id": self.id})
