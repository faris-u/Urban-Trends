from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from AdminApp.models import *
from UserApp.models import *



def admin_login(request):
    if request.method=='POST':
        admin_name=request.POST.get('username')
        admin_password=request.POST.get('password')
        admin=AdminModel.objects.filter(admin_name=admin_name,admin_password=admin_password).first()
        if admin:
            request.session['admin_id']=admin.admin_id
            return redirect('project_admin')
        else:
            return redirect('admin_login')
    return render(request,'admin_login.html')

def project_admin(request):
    if 'admin_id' in request.session:
        products=Product.objects.count()
        users=UserModel.objects.count()
        return render(request,'admin.html',{'products':products,'users':users})
    else:
        return redirect('admin_login')

def products(request):
    if 'admin_id' in request.session:
        products=Product.objects.all()
        return render(request,'products.html',{'products':products})
    else:
        return redirect('admin_login')


def remove_product(request, product_id):
    product = Product.objects.get(product_id=product_id)
    product.delete()
    return redirect('/products')


def users(request):
    users=UserModel.objects.all()
    return render(request,'users.html',{'users':users})

def remove_user(request,user_id):
    user=UserModel.objects.get(user_id=user_id)
    user.delete()
    return redirect('/users')
