from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def product_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'title': obj.name,
        'description': obj.description,
        'image': obj.image,
        'price': obj.price,
    }
    return render(request, "products/details.html", context)
