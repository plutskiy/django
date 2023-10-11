from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from shopapp.models import Producs, Order


def shop_index(request:HttpRequest):
    products = [
        ('Desktop', 3000),
        ('Dyson', 500),
        ('iPhone', 999),
        ('TV', 5999),

    ]
    context = {
        'products' : products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)

def products_list(request: HttpRequest):
    context = {
        "products" : Producs.objects.all()
    }
    return render(request, 'shopapp/products-list.html', context=context)

def orders_list(request: HttpRequest):
    context ={
        'orders' : Order.objects.select_related("user_id").prefetch_related("products").all()
    }
    return render(request, 'shopapp/orders-list.html', context=context)