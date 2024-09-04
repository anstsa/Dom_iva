from django.shortcuts import render
from goods.models import Product


def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Product.objects.all()
    else:
        goods = Product.objects.filter(category__slug = category_slug)
        context = {
        "title": "Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    produc = Product.objects.get(slug = product_slug)
    context = {
        'product': produc   
    }
    return render(request, "goods/product.html", context = context)
