from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from SellerApp.models import *
from django.db.models import Q
from UserApp.models import *
from datetime import datetime
from .models import CartModel



# Create your views here.


from django.shortcuts import render
from django.db.models import Q
from .models import UserModel, Product

def home(request):
    user = None  # Initialize user to None

    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user = UserModel.objects.get(pk=user_id)
        username = user.username

    if request.method == 'POST':
        search_value = request.POST.get('search')
        if search_value:
            products = Product.objects.filter(
                Q(product_title__icontains=search_value) |
                Q(product_description__icontains=search_value) |
                Q(seller_id__seller_name__icontains=search_value)
            )
            return render(request, 'search.html', {'products': products})

    # Fetching all products along with their corresponding images
    products_with_images = Product.objects.prefetch_related('productimage_set').all().order_by('?')[:4]

    # Create a dictionary to store product data with images
    products_data = {}

    # Iterate over fetched products
    for product in products_with_images:
        product_images = product.productimage_set.all()  # Accessing related images for each product
        images_urls = [img.product_image1.url for img in product_images]  # Get URLs of images for the product

        # Store product data and associated image URLs in the dictionary
        products_data[product.product_id] = {
            'product_id': product.product_id,  # Include product_id in the dictionary
            'title': product.product_title,
            'description': product.product_description,
            'price': product.product_price,
            'quantity': product.product_quantity,
            'image_urls': images_urls
        }

    return render(request, 'home.html', {'products_data': products_data, 'user': user})

def top(request):
    # data = Product.objects.filter(product_id=id)

    # Query for the SubCategoryModel instance corresponding to the category "Top Wear"
    top_wear_category = MainCategory.objects.get(main_category_description="Top Wear")

    # Retrieve all SubCategoryModel instances belonging to the "Top Wear" main category
    top_wear_subcategories = top_wear_category.subcategorymodel_set.all()

    # Retrieve all Product instances belonging to the subcategories under the "Top Wear" main category
    top_wear_products = Product.objects.filter(subcategory_id__in=top_wear_subcategories)

    # Initialize a list to store product details (title, price, image_url)
    top_wear_products_data = []
    # print(top_wear_products_data)

    # Iterate over each product and fetch its associated image and other details
    for product in top_wear_products:
        print('hiihih')
        # Retrieve images associated with the current product
        product_images = ProductImage.objects.filter(product_id=product)

        # Extract the first image URL if available
        image_url = product_images.first().product_image1.url if product_images else None

        # Append product details to the list
        top_wear_products_data.append({
            'id': product.product_id,
            'title': product.product_title,
            'price': product.product_price,
            'image_url': image_url
        })
        print(top_wear_products_data)

        if request.method=='POST':

            value=request.POST.get('Sort')

            if value=='asc':
                top_wear_products_data=top_wear_products_data.order_by('product_price')

            if value=='desc':
                top_wear_products_data=top_wear_products_data.order_by('-product_price')



    # Pass the data to the template
    return render(request, 'top.html', {'top_wear_products_data': top_wear_products_data})
    # return render(request,'product_view.html',{'data':data})


def bottom(request):
    # Query for the SubCategoryModel instance corresponding to the category "Bottom Wear"
    bottom_wear_category = MainCategory.objects.get(main_category_description="Bottom Wear")

    # Retrieve all SubCategoryModel instances belonging to the "Top Wear" main category
    bottom_wear_subcategories = bottom_wear_category.subcategorymodel_set.all()

    # Retrieve all Product instances belonging to the subcategories under the "Top Wear" main category
    bottom_wear_products = Product.objects.filter(subcategory_id__in=bottom_wear_subcategories)

    # Initialize a list to store product details (title, price, image_url)
    bottom_wear_products_data = []

    # Iterate over each product and fetch its associated image and other details
    for product in bottom_wear_products:
        # Retrieve images associated with the current product
        product_images = ProductImage.objects.filter(product_id=product)

        # Extract the first image URL if available
        image_url = product_images.first().product_image1.url if product_images else None

        # Append product details to the list
        bottom_wear_products_data.append({
            'id': product.product_id,
            'title': product.product_title,
            'price': product.product_price,
            'image_url': image_url
        })

    # Pass the data to the template
    return render(request, 'bottom.html', {'bottom_wear_products_data': bottom_wear_products_data})


def inner(request):
    # Query for the SubCategoryModel instance corresponding to the category "Inner Wear"
    inner_wear_category = MainCategory.objects.get(main_category_description="Inner Wear")

    # Retrieve all SubCategoryModel instances belonging to the "Top Wear" main category
    inner_wear_subcategories = inner_wear_category.subcategorymodel_set.all()

    # Retrieve all Product instances belonging to the subcategories under the "Top Wear" main category
    inner_wear_products = Product.objects.filter(subcategory_id__in=inner_wear_subcategories)

    # Initialize a list to store product details (title, price, image_url)
    inner_wear_products_data = []

    # Iterate over each product and fetch its associated image and other details
    for product in inner_wear_products:
        # Retrieve images associated with the current product
        product_images = ProductImage.objects.filter(product_id=product)

        # Extract the first image URL if available
        image_url = product_images.first().product_image1.url if product_images else None

        # Append product details to the list
        inner_wear_products_data.append({
            'id': product.product_id,
            'title': product.product_title,
            'price': product.product_price,
            'image_url': image_url
        })

    # Pass the data to the template
    return render(request, 'inner.html', {'inner_wear_products_data': inner_wear_products_data})


def accessories(request):
    # Query for the SubCategoryModel instance corresponding to the category "Inner Wear"
    accessories_category = MainCategory.objects.get(main_category_description="Accessories")

    # Retrieve all SubCategoryModel instances belonging to the "Top Wear" main category
    accessories_subcategories = accessories_category.subcategorymodel_set.all()

    # Retrieve all Product instances belonging to the subcategories under the "Top Wear" main category
    accessories_products = Product.objects.filter(subcategory_id__in=accessories_subcategories)

    # Initialize a list to store product details (title, price, image_url)
    accessories_products_data = []

    # Iterate over each product and fetch its associated image and other details
    for product in accessories_products:
        # Retrieve images associated with the current product
        product_images = ProductImage.objects.filter(product_id=product)

        # Extract the first image URL if available
        image_url = product_images.first().product_image1.url if product_images else None

        # Append product details to the list
        accessories_products_data.append({
            'id': product.product_id,
            'title': product.product_title,
            'price': product.product_price,
            'image_url': image_url
        })

    # Pass the data to the template
    return render(request, 'accessories.html', {'accessories_products_data': accessories_products_data})


# def product_view(request,id):
#
#
#     data=Product.objects.filter(product_id=id)
#     print(data)
#
#
#     return render(request,'product_view.html',{'data':data})

def product_view(request, id):
    product = get_object_or_404(Product, product_id=id)
    images = ProductImage.objects.filter(product_id=product)
    review = ReviewModel.objects.filter(product_id=id)
    size= Size.objects.all()
    context = {
        'product': product,
        'images': images,
        'size' : size,
        'review':review
    }
    return render(request, 'product_view.html', context)




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserModel.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.user_id
            return redirect('/')
        else:
            return redirect('/login')

    return render(request, 'login.html')

def logout(request):
    print("logout fun called")
    del request.session['user_id']
    return redirect('/')


def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        save=UserModel()
        save.username=username
        save.password=password
        save.phone_number=phone_number
        save.email=email
        save.create_at=datetime.now()
        save.save()
        return redirect('/login')
    return render(request,'signin.html')



def profile(request):
    # Check if user ID is present in session
    user_id = request.session.get('user_id')
    if user_id:
        # Query the database to get user details
        user = UserModel.objects.filter(user_id=user_id).first()
        address=UserAddress.objects.filter(user_id=user_id)
        if request.method == 'POST':
            # Get the existing user instance
            update = UserModel.objects.get(user_id=user_id)
            # Update user details
            update.username = request.POST.get('username')
            update.phone_number = request.POST.get('phone')
            update.email = request.POST.get('email')
            update.password = request.POST.get('password')
            update.create_at = datetime.now()
            # Handle user image update
            new_image = request.FILES.get('new_image')
            if new_image:
                update.user_image = new_image
            update.save()
            return redirect('/profile')
        # Pass user details to the template
        return render(request, 'profile.html', {'user': user,'address':address})
    else:
        # Handle the case when user is not logged in
        return render(request, 'not_logged_in.html')


def address(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        user = UserModel.objects.get(user_id=user_id)  # Fetching a single user
        address = UserAddress.objects.filter(user_id=user_id)

        return render(request, 'address.html', {'user': user, 'address': address})



def update_address(request,address_id):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')

        user = UserModel.objects.get(user_id=user_id)  # Fetching a single user
        address = UserAddress.objects.filter(user_id=user_id,address_id=address_id)
        if request.method == 'POST':
            update = UserAddress.objects.get(user_id=user_id,address_id=address_id)  # Fetch the specific address to update
            update.user_address = request.POST.get('address')
            update.user_location = request.POST.get('location')
            update.user_pincode = request.POST.get('pin')
            update.user_city = request.POST.get('city')
            update.user_district = request.POST.get('district')
            update.user_state = request.POST.get('state')
            update.user_address_type = request.POST.get('type')
            update.user_landmark = request.POST.get('landmark')
            update.save()
            return redirect('/address')  # Redirect to the address page after updating
        return render(request, 'update_address.html', {'user': user, 'address': address})



def add_address(request):
    if 'user_id' in request.session:
        user = UserModel.objects.get(user_id=request.session['user_id'])
        if request.method == 'POST':
            # Update user address details
            address = UserAddress()
            address.user_id_id = request.session.get('user_id')
            address.user_address = request.POST.get('address')
            address.user_location = request.POST.get('location')
            address.user_pincode = request.POST.get('pin')
            address.user_city = request.POST.get('city')
            address.user_district = request.POST.get('district')
            address.user_state = request.POST.get('state')
            address.user_address_type = request.POST.get('type')
            address.user_landmark = request.POST.get('landmark')

            address.save()
            return redirect('/address')
        return render(request, 'add_address.html', {'user': user})






def remove_address(request,address_id):
    address=UserAddress.objects.get(address_id=address_id)
    address.delete()
    return redirect('/address')



def cart(request, product_id):
    if 'user_id' in request.session:
        if request.method == 'POST':
            # Retrieve quantity and size from the form data
            quantity = int(request.POST.get('quantity'))
            size = request.POST.get('size')

            # Retrieve user ID from the session
            user_id = request.session['user_id']

            try:
                # Retrieve the product from the database
                product = Product.objects.get(product_id=product_id)
                price = product.product_price
            except Product.DoesNotExist:
                return HttpResponse("Product not found")

            # Calculate total price
            total = quantity * price

            # Create a new cart item and save it to the database
            cart_item = CartModel.objects.create(
                quantity=quantity,
                user_id_id=user_id,
                product_id=product,
                size=size,
                datetime=datetime.now(),

            )

            return HttpResponse("Added to cart successfully!")
        else:
            # Only allow POST requests for adding items to the cart
            return HttpResponse("Method not allowed")
    else:
        # Redirect unauthenticated users to the login page
        return redirect('/login')

def rem_cart(request,cart_id):
    if 'user_id' in request.session:
        cart_item = CartModel.objects.get(cart_id=cart_id)
        cart_item.delete()
        return redirect('/showcart')
    else:
        return redirect('/login')



def showcart(request):
    if 'user_id' in request.session:
        # Fetch cart items along with related product and product images
        cart_items = CartModel.objects.filter(user_id=request.session['user_id']).all()
        productd=[]
        for items in cart_items:
            img=ProductImage.objects.get(product_id=items.product_id.product_id)
            productd.append({
                "items":items,
                "img":img
            })







        return render(request, 'showcart.html', {"data":productd,"cart":cart_items})
    else:
        return redirect('/login')


def wishlist(request,product_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        product = Product.objects.get(product_id=product_id)
        wishlist_item = WishlistModel.objects.create(
            user_id_id=user_id,
            product_id=product,

        )
        return redirect('/show_wishlist')
    else:
        return redirect('/login')


def show_wishlist(request):
    if 'user_id' in request.session:
        wishlist_items = WishlistModel.objects.filter(user_id=request.session['user_id']).all()
        wishlistd=[]
        for items in wishlist_items:
            img=ProductImage.objects.get(product_id=items.product_id.product_id)
            wishlistd.append({
                "items":items,
                "img":img
            })
        return render(request,'show_wishlist.html', {'wishlist_items': wishlist_items,'data':wishlistd})
    else:
        return redirect('/login')


def remove_wishlist(request,wishlist_id):
    if 'user_id' in request.session:
        wishlist_item = WishlistModel.objects.get(wishlist_id=wishlist_id)
        wishlist_item.delete()
        return redirect('/show_wishlist')


def buynow(request, product_id):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        address = UserAddress.objects.filter(user_id=user_id)
        product = Product.objects.get(product_id=product_id)
        img = ProductImage.objects.get(product_id=product_id)


        if request.method=='POST':
            quantity = request.POST.get('quantity')

            buy_item = BuyProduct.objects.create(
                user_id_id=user_id,
                product_id=product,
                address_id=UserAddress.objects.get(address_id=request.POST.get('address')),
                date=datetime.now(),
                quantity = quantity
            )

            return redirect('/showbuy')






        return render(request, 'buynow.html', {'product': product, 'address': address,'img':img })
    else:
        return redirect('/login')

def showbuy(request):
    if 'user_id' in request.session:
        buy_items = BuyProduct.objects.filter(user_id=request.session['user_id']).all()

        buyd=[]
        for items in buy_items:
            img=ProductImage.objects.get(product_id=items.product_id.product_id)
            buyd.append({
                "items":items,
                "img":img
            })
        return render(request,'showbuy.html', {'buy_items': buy_items,'data':buyd})
    else:
        return redirect('/login')




def add_review(request, product_id):
    if 'user_id' in request.session:
        user_data = UserModel.objects.filter(user_id=request.session['user_id'])
        product_data = Product.objects.filter(product_id=product_id)
        img = ProductImage.objects.get(product_id=product_id)
        data=[]



        existing_order = BuyProduct.objects.filter(product_id=product_id, user_id=user_data.first())
        for img in existing_order:
            img=ProductImage.objects.get(product_id=img.product_id.product_id)
            data.append({
                "img":img
            })
        if existing_order.exists():
            if request.method == 'POST':
                myreview = ReviewModel()
                myreview.user_id_id = request.session['user_id']
                myreview.product_id = Product.objects.get(product_id=product_id)
               
                myreview.review = request.POST.get('review')
                myreview.save()
                return redirect('/')

        else:
            return HttpResponse('you havent bought this product yet')


        return render(request, 'add_review.html',{'product': product_data,'order':user_data,'data':data,'img':img})
    else:
        return redirect('/login')















