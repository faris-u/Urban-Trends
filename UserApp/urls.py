from django.urls import path
from UserApp import views

urlpatterns = [
    path('',views.home),
    path('top',views.top,name='top_path'),
    path('bottom',views.bottom,name='bottom_path'),
    path('inner',views.inner,name='inner_path'),
    path('accessories',views.accessories,name='accessories_path'),
    path('product_view/<int:id>', views.product_view),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signin',views.signin,name='signin'),
    path('profile',views.profile,name='profile'),
    path('cart/<int:product_id>',views.cart,name='cart'),
    path('showcart',views.showcart,name='showcart'),
    path('remove_cart/<int:cart_id>',views.rem_cart,name='rem_cart'),
    path('address',views.address,name='address'),
    path('update_address/<int:address_id>',views.update_address,name='update_address'),
    path('add_address',views.add_address,name='add_address'),
    path('remove_address/<int:address_id>',views.remove_address,name='remove_address'),
    path('wishlist/<int:product_id>',views.wishlist,name='wishlist'),
    path('show_wishlist',views.show_wishlist,name='show_wishlist'),
    path('remove_wishlist/<int:wishlist_id>',views.remove_wishlist,name='remove_wishlist'),
    path('buynow/<int:product_id>',views.buynow,name='buynow'),
    path('showbuy',views.showbuy,name='showbuy'),
    path('add_review/<int:product_id>',views.add_review,name='add_review')
]