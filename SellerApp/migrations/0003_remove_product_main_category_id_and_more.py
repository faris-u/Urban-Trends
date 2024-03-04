# Generated by Django 5.0.1 on 2024-02-07 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellerApp', '0002_product_main_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='main_category_id',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SellerApp.subcategorymodel'),
        ),
    ]
