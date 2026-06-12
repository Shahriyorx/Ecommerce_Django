from django.shortcuts import render

from apps.products.models import Product

def get_products(request):
    products = [i.to_dict() for i in Product.objects.all()]
    print(products)
    return render(request, 'products/product_list.html', {'products': products})