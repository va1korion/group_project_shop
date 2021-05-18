from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MyUser(User):
    birth_date = models.DateField()
    cart = models.OneToOneField('cart.Cart', on_delete=models.CASCADE, related_name='my_cart', null=True)
    order_history = models.JSONField()
