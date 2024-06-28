from django.shortcuts import render, get_object_or_404
from .models import Item, Category


def cafe(request):
    categories = Category.objects.all()
    return render(request, 'cafe.html',{'categories': categories})


def ccategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Item.objects.filter(category=category)
    return render(request, 'citem.html', {'products': products})
