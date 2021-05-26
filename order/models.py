from django.db import models
from django.urls import reverse

from users.models import MyUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Order(models.Model):
    items = models.JSONField()
    owner = models.ForeignKey(to=MyUser, null=False, on_delete=models.CASCADE)
    # date = models.DateTimeField(auto_now_add=True)
    # edit = models.DateTimeField(auto_now=True)

    class Status(models.TextChoices):
        PENDING = 'PE', _('Pending')
        CONFIRMED = 'PA', _('Confirmed')
        DELIVERED = 'DL', _('Delivered')
        CANCELLED = 'CA', _('Cancelled')

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def get_absolute_url(self):
        return reverse("Order", kwargs={"id": self.id})
