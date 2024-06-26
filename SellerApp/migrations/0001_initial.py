# Generated by Django 5.0.1 on 2024-02-06 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('main_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('main_category_description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'main_category_table',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=300)),
                ('product_quantity', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product_table',
            },
        ),
        migrations.CreateModel(
            name='SellerModel',
            fields=[
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=200)),
                ('seller_password', models.CharField(max_length=100)),
                ('seller_email', models.EmailField(max_length=254)),
                ('seller_status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'seller_table',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('product_image_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_image', models.ImageField(upload_to='seller/')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.product')),
            ],
            options={
                'db_table': 'product_image_table',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.sellermodel'),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('size_id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=50)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.product')),
            ],
            options={
                'db_table': 'size_table',
            },
        ),
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('subcategory_id', models.AutoField(primary_key=True, serialize=False)),
                ('subcategory_description', models.CharField(max_length=200)),
                ('main_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.maincategory')),
            ],
            options={
                'db_table': 'subcategory_table',
            },
        ),
    ]
