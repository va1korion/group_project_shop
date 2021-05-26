from django.contrib.auth import admin
from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='myuser', null=True, blank=True)
    cart = models.JSONField(default=list)
    order_history = models.JSONField(default=list)
    identifier = models.AutoField(primary_key=True)
