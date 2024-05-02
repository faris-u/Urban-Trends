from django.db import models
from SellerApp.models import *
from UserApp.models import *
from datetime import datetime




# Create your models here.
class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    user_image = models.ImageField(upload_to='user/',null=True)
    create_at = models.DateTimeField()
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_table'


class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_address = models.CharField(max_length=200)
    user_location = models.CharField(max_length=200)
    user_pincode = models.CharField(max_length=100)
    user_city = models.CharField(max_length=200)
    user_district = models.CharField(max_length=200)
    user_state = models.CharField(max_length=200)
    user_landmark = models.CharField(max_length=300)
    user_address_type = models.CharField(max_length=100)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'user_address_table'


class BuyProduct(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    address_id = models.ForeignKey(UserAddress, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'buy_product_table'


class WishlistModel(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlist_table'



class CartModel(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(max_length=5, null=True)
    datetime = models.DateTimeField(auto_created=True)


    class Meta:
        db_table = 'cart_table'


class ReviewModel(models.Model):
    review_id = models.AutoField(primary_key=True)
    review = models.CharField(max_length=300)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review_table'

#
# class Payment(models.Model):
#     payment_id = models.AutoField(primary_key=True)
#     payment_type = models.CharField(max_length=100)
#     datetime = models.DateTimeField()
#     order_id = models.ForeignKey(BuyProduct, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'payment_table'
