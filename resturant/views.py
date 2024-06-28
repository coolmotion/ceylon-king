from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item, Category


def resturant(request):
    categories = Category.objects.all()
    return render(request, 'resturant.html', {'categories': categories})


def rcategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Item.objects.filter(category=category)
    return render(request, 'item.html', {'products': products})
    # return HttpResponse("hello world!")