from django.urls import path
from SellerApp import views

urlpatterns = [
    path('', views.seller_login),
    path('seller/', views.seller, name='seller'),
    path('add_product/', views.add_product, name='add_product'),
]
