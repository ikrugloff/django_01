from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'page_title': 'Магазин/главная'
    }
    return render(request, 'mainapp/index.html', context)  # / в начале не ставится, т.к. адрес относительный корня
    # для шаблонов


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')
