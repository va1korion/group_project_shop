from django.shortcuts import render, get_object_or_404
from order.models import Order


def order_view(request, id):
    obj = get_object_or_404(Order, id=id)
    context = {
        'id': obj.id,
        'items': obj.items,
        'status': obj.status,
        # 'date': obj.date,
        # 'edited': obj.edit,
    }
    return render(request, "order", context)
