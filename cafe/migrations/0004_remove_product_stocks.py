# Generated by Django 5.0.6 on 2024-06-17 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_alter_product_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stocks',
        ),
    ]