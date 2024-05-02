from django.db import models
from UserApp .models import *


# Create your models here.
class SellerModel(models.Model):
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=200)
    seller_password = models.CharField(max_length=100)
    seller_email = models.EmailField()
    seller_status = models.BooleanField(default=True)

    def __str__(self):
        return self.seller_name

    class Meta:
        db_table = 'seller_table'


class MainCategory(models.Model):
    main_category_id = models.AutoField(primary_key=True)
    main_category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.main_category_description

    class Meta:
        db_table = 'main_category_table'




class SubCategoryModel(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_description = models.CharField(max_length=200)
    main_category_id = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_description

    class Meta:
        db_table = 'subcategory_table'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=200)
    product_description = models.CharField(max_length=300)
    product_quantity = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    seller_id = models.ForeignKey(SellerModel,on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(SubCategoryModel,on_delete=models.CASCADE,null=True)
    images = models.ManyToManyField('ProductImage', related_name='images', blank=True)
    def __str__(self):
        return self.product_title

    class Meta:
        db_table = 'product_table'


class ProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product_image1 = models.ImageField(upload_to='seller/' ,null=True)
    product_image2 = models.ImageField(upload_to='seller/' ,null=True)
    product_image3 = models.ImageField(upload_to='seller/' ,null=True)
    product_image4 = models.ImageField(upload_to='seller/' ,null=True)

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.product_id)

    class Meta:
        db_table = 'product_image_table'


class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=50)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)




    def __str__(self):
        return (self.size)

    class Meta:
        db_table = 'size_table'



