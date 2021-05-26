import json

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from users.models import MyUser
from .models import Product
import django.forms as forms


class BuyButton(forms.Form):
    btn = forms.Field()


# Create your views here.
def product_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'title': obj.name,
        'description': obj.description,
        'image': obj.image,
        'price': obj.price,
    }
    if request.method == "POST":
        if request.user.is_authenticated:
            user = get_object_or_404(User, username=request.user.username)
            user.myuser.cart.append((obj.name, float(obj.price), obj.id))
            print(user.myuser.cart)
            user.myuser.save()
            obj.quantity -= 1
            obj.save()
            print(obj.quantity)

    return render(request, "products/details.html", context)
