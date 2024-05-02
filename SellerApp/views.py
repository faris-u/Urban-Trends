from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from SellerApp.models import *



def seller_login(request):
    if request.method == 'POST':
        seller_name = request.POST.get('seller_name')
        seller_password = request.POST.get('seller_password')
        seller = SellerModel.objects.filter(seller_name=seller_name, seller_password=seller_password).first()
        if seller:
            request.session['seller_id'] = seller.seller_id
            return redirect('seller')
        else:
            return redirect('seller_login')

    return render(request, 'seller_login.html')
def seller(request):
    if 'seller_id' in request.session:
        seller_data = SellerModel.objects.filter(seller_id=request.session['seller_id'])
        seller_products = Product.objects.filter(seller_id = request.session['seller_id'])
        return render(request,'seller.html', {'seller_data': seller_data,"seller_products":seller_products})

    else:
        return redirect('seller_login')

def add_product(request):
    if 'seller_id' in request.session:
        if request.method=='POST':
            new_product=Product()
            new_product.product_title=request.POST.get('title')
            new_product.product_description=request.POST.get('description')
            new_product.product_quantity=request.POST.get('qty')
            new_product.product_price=request.POST.get('price')
            new_product.seller_id_id=request.session.get('seller_id')
            new_product.save()


            return redirect('seller')
        return render(request, 'add_product.html')


