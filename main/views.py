from django.shortcuts import render

def index(request):
    context = {
        'title': 'Дом Ивы',
        'content': 'Магазин рукоделий Дом Ивы',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'Информация о нас',
        'text_on_page': 'Красткая информация о том какой хороший магазин и тавары',
    }
    return render(request, 'main/about.html', context)
