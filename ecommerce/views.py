from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ecommerce_index_view(request):
   '''This function render index page of ecommerce views'''
   return HttpResponse('Welcome to 6410742651 Peerapat Suttiprasit views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id,
    }
    return render(request, 'index.html', context=context_data)

def home_view(req):
    return render(req, 'homepage.html')
def category_view(req):
    return render(req, 'category.html')
def product_view(req):
    # In your views.py or context data
    products = [
    {
        'name': 'Product 1',
        'description': 'Description for Product 1',
        'image_url': 'https://computechstore.in/wp-content/uploads/2022/10/h1000-black-image-main-600x600-1.png',
    },
    {
        'name': 'Product 2',
        'description': 'Description for Product 2',
        'image_url': 'https://cdn.ut.in.th/media/catalog/product/cache/3e7ad5c85ed3f6d2f11e07e514d0d486/h/y/hyperx-cloud-core-dts-1.png',
    },
    {
        'name': 'Product 3',
        'description': 'Description for Product 3',
        'image_url': 'https://elitehubs.com/cdn/shop/products/rog-fusion-ii-500-image-1-600x600-1.webp?v=1695312374',
    },
    {
        'name': 'Product 4',
        'description': 'Description for Product 4',
        'image_url': 'https://telefonika.com/wp-content/uploads/2021/02/Sony-MDR-G300WZEH3-Wired-Gaming-Headset-600x600.jpg',
    },
    {
        'name': 'Product 5',
        'description': 'Description for Product 5',
        'image_url': 'https://www.myithub.com.au/wp-content/uploads/2020/02/Untitled-design-2020-02-24T120712.503-600x600.jpg',
    },
    {
        'name': 'Product 6',
        'description': 'Description for Product 6',
        'image_url': 'https://www.samma3a.com/media/catalog/product/cache/53bce20d7ffd193e694a37d8959f20c7/a/r/arctis_pro_1_.jpg',
    },
    ]
    return render(req, 'product.html', context={'products': products})
def checkout_view(req):
    return render(req, 'checkout.html')
def contact_view(req):
    return render(req, 'contact.html')