from django.shortcuts import render,redirect, get_object_or_404
from SellerApp.models import *
from django.db.models import Q

# Create your views here.


def home(request):

    if request.method=='POST':
        data=Product.objects.all()
        search_value = request.POST.get('search')
        product=Product.objects.filter(Q(product_title__icontains=search_value)|Q(product_description__icontains=search_value)| Q(seller_id__seller_name__icontains=search_value))

        return render(request,'search.html',{'product':product,'data':data})

    # Fetching all products along with their corresponding images
    products_with_images = Product.objects.prefetch_related('productimage_set').all().order_by('?')[:4]

    # Create a dictionary to store product data with images
    products_data = {}

    # Iterate over fetched products
    for product in products_with_images:
        product_images = product.productimage_set.all()  # Accessing related images for each product
        images_urls = [img.product_image.url for img in product_images]  # Get URLs of images for the product

        # Store product data and associated image URLs in the dictionary
        products_data[product.product_id] = {
            'title': product.product_title,
            'description': product.product_description,
            'price': product.product_price,
            'quantity': product.product_quantity,
            'image_urls': images_urls
        }

    return render(request, 'home.html', {'products_data': products_data})



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
        image_url = product_images.first().product_image.url if product_images else None

        # Append product details to the list
        top_wear_products_data.append({
            'id':product.product_id,
            'title': product.product_title,
            'price': product.product_price,
            'image_url': image_url
        })
        print(top_wear_products_data)




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
        image_url = product_images.first().product_image.url if product_images else None

        # Append product details to the list
        bottom_wear_products_data.append({
            'id':product.product_id,
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
        image_url = product_images.first().product_image.url if product_images else None

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
        image_url = product_images.first().product_image.url if product_images else None

        # Append product details to the list
        accessories_products_data.append({
            'id': product.product_id,
            'title': product.product_title,
            'price': product.product_price,
            'image_url': image_url
        })

    # Pass the data to the template
    return render(request, 'accessories.html', {'accessories_products_data': accessories_products_data})

def product_view(request,id):


    data=Product.objects.filter(product_id=id)
    print(data)


    return render(request,'product_view.html',{'data':data})

