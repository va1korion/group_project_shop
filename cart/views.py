from django.shortcuts import render, get_object_or_404
from .models import Cart
# Create your views here.


def cart_view(request):
    if request.user.is_authenticated:
        obj = get_object_or_404(Cart, user=request.user)
        context = {
            'User': obj.user.username,
            'items': obj.items
        }
        return render(request, "cart", context)
    else:
        return render(request, "not_logged_in", {})

