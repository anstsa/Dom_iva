from django.shortcuts import render

from goods.models import Product

goods = Product.objects.all()



def catalog(request):
    context = {
        "title": "Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
