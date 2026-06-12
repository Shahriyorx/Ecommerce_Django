from django.shortcuts import render

from apps.products.models import *

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    data = {
        'categories': categories,
        'products': products,
    }
        
    return render(request, 'common/home.html')