from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories
# Create your views here.


def index(request):

    context: dict[str, str] = {
        'title': 'Thetl - Главная',
        'content': 'Магазин технологий TheTl',

    }
    return render(request, 'main/index.html', context)


def about(request):

    context: dict[str, str] = {
        'title': 'Thetl - О нас',
        'content': 'О нас',
        'text_on_page': 'еуууууу'
    }
    return render(request, 'main/about.html', context)