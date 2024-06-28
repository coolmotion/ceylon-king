from django.urls import path
from . import views

urlpatterns = [
    path('', views.cafe, name='cafe'),
    path('category/<int:category_id>', views.ccategory, name='ccategory'),

]
