from django.urls import path
from AdminApp import views

urlpatterns = [
    path('', views.admin_login,name='admin_login'),
    path('/project_admin', views.project_admin,name='project_admin'),
    path('/products',views.products,name="products"),
    path('/project_admin/remove_product/<int:product_id>',views.remove_product,name='remove_product'),
    path('/users',views.users,name='users'),
    path('/remove_user/<int:user_id>',views.remove_user,name='remove_user')

]
