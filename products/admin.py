from django.contrib import admin

from order.models import Order
from users.models import MyUser
from .models import Product
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(Product)
admin.site.register(Order)


class UserInLine(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'employee'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserInLine,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
