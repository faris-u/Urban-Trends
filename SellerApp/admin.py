from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SellerModel)
admin.site.register(MainCategory)
admin.site.register(SubCategoryModel)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Size)
