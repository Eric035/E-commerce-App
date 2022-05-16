from django.shortcuts import render
from .models import *

# Create your views here.


def estore(request):
    products = Product.objects.all()
    return render(request, 'estore/estore.html', context={'products': products})


def checkout(request):
    return render(request, 'estore/checkout.html')


def cart(request):
    items = []
    if request.user.authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, delivered=False)
        items = order.orderitem_set.all()

    return render(request, 'estore/cart.html', context={'items': items})
