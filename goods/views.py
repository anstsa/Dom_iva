from django.shortcuts import render
from django.template import context

from goods.models import Product

goods = Product.objects.all()



def catalog(request):
    context = {
        "title": "Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Product.objects.get(slug = product_slug)
   
    context = {
        'product': product    
    }
    return render(request, "goods/product.html", context = context)
