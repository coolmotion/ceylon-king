from django.urls import path
from . import views

urlpatterns = [
    path('', views.resturant, name='resturant'),
    path('category/<int:category_id>', views.rcategory, name='rcategory'),
]
