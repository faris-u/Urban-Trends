# Generated by Django 5.0.1 on 2024-02-06 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SellerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('user_image', models.ImageField(upload_to='user/')),
                ('create_at', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_address', models.CharField(max_length=200)),
                ('user_location', models.CharField(max_length=200)),
                ('user_pincode', models.CharField(max_length=100)),
                ('user_city', models.CharField(max_length=200)),
                ('user_district', models.CharField(max_length=200)),
                ('user_state', models.CharField(max_length=200)),
                ('user_landmark', models.CharField(max_length=300)),
                ('user_address_type', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'user_address_table',
            },
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(max_length=300)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'review_table',
            },
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('datetime', models.DateTimeField(auto_created=True)),
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'cart_table',
            },
        ),
        migrations.CreateModel(
            name='BuyProduct',
            fields=[
                ('date', models.DateTimeField(auto_created=True)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.ImageField(upload_to='')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerApp.product')),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.useraddress')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'buy_product_table',
            },
        ),
    ]