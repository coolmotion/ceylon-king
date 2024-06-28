from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/resturant/categories/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100, blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/resturant/products/')

    def __str__(self):
        return self.name
