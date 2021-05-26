from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
# Create your views here.
from django.utils.datetime_safe import time

from order.models import Order
from users.models import MyUser
from users.views import personal_view


class BuyButton(forms.Form):
    btn = forms.BooleanField()


def cart_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        obj = user.myuser
        total = 0
        price_list = []
        item_list = []
        id_list = []
        if obj.cart:
            for item in obj.cart:
                total += item[1]
                price_list.append(item[1])
                item_list.append(item[0])
                id_list.append(item[2])
        context = {
            'items': obj.cart,
            'item_list': item_list,
            'price_list': price_list,
            'total': total
        }
        if request.method == 'POST':

            if request.user.is_authenticated:
                order = Order.objects.create(owner=request.user, items=item_list)
                obj.order_history.append(order.id)
                obj.cart = []
                obj.save()
                return redirect(personal_view)

        return render(request, "cart/cart.html", context)
    else:
        return render(request, "not_logged_in/not_logged_in.html", {})

