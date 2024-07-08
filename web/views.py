from django.shortcuts import render
from resturant.models import Category


def index(request):
    return render(request, 'index.html')


def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def about(request):
    return render(request, 'about.html')
