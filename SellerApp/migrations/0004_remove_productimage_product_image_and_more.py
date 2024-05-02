# Generated by Django 5.0.1 on 2024-03-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellerApp', '0003_remove_product_main_category_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='size',
            name='product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='SellerApp.productimage'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product_image1',
            field=models.ImageField(null=True, upload_to='seller/'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product_image2',
            field=models.ImageField(null=True, upload_to='seller/'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product_image3',
            field=models.ImageField(null=True, upload_to='seller/'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product_image4',
            field=models.ImageField(null=True, upload_to='seller/'),
        ),
    ]