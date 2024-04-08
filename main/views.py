from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title' : 'HOME - главная',
        'content' : 'Магазин мебели HOME' ,
    }

    return render(request , 'main/index.html' , context)

def about(request):
    context = {
        'title' : 'HOME - О нас',
        'content' : 'О нас',
        'text_on_page' : 'Текст о том почему наш магазин хороший'
    }
    return render(request , 'main/about.html' , context)


