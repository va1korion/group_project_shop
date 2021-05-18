from django.db import models


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField('users.MyUser', on_delete=models.CASCADE, related_name='my_user')
    items = models.JSONField(null=True)
