from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .cart import Cart
from resturant.models import Product
from django.http import JsonResponse
import json


def cart_summary(request):
    return render(request, 'cart.html', {})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        respone = JsonResponse({'Product Name': product.name})
        return respone


def cart_addlist(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_ids = request.POST.get('product_ids')
        product_ids = json.loads(product_ids)

        added_products = []

        for product_id in product_ids:
            product = get_object_or_404(Product, id=product_id)
            cart.add(product=product)
            added_products.append(product.name)

    response = JsonResponse({'Added Products': added_products})
    return response


def cart_delete(request):
    return HttpResponse("Item deleted from cart.")


def cart_update(request):
    return HttpResponse("Cart updated successfully.")
