
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Product
from goods.utils import q_search



def catalog(request, category_slug=None):

    page = request.GET.get('page',1) #получили гет запрос page
    on_sale = request.GET.get('on_sale', None) #получили гет для фильтрации по скидкам
    order_by = request.GET.get('order_by', None) #получили гет для фильтрации по убыванию, возрастанию
    query = request.GET.get('q', None) #получили  get запрос для поиска

    if category_slug == 'all':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug = category_slug)) #если товаров нет в категории выводит ошибку 404

    if on_sale:
        goods = Product.objects.filter(discount__gt = 0)

    if order_by and order_by != 'default':
        goods = Product.objects.order_by(order_by)

    paginator = Paginator(goods,3) #выволится три товара на  страницу
    current_page = paginator.page(int(page))  #какая страница с товароми отображено 1,2,3,
    context = {
        "title": "Каталог",
        "goods": current_page, #выводит криресет только столько сколько отображено в пагинации
        "slug_url": category_slug, #дополнительный параметр для url адреса
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    produc = Product.objects.get(slug = product_slug)
    context = {
        'product': produc   
    }
    return render(request, "goods/product.html", context = context)
