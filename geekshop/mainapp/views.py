from django.shortcuts import render, HttpResponseRedirect
from mainapp.models import ProductCategory, Product
from django.urls import reverse


def index(request):
    context = {
        'page_title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    products = Product.objects.all()

    context = {
        'page_title': 'каталог',
        'products': products
    }
    return render(request, 'mainapp/products.html', context)


def category(request, pk):
    print(f'выбрали {pk}')
    return HttpResponseRedirect(reverse('main:products'))


def contact(request):
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД'
        },
        {
            'city': 'Санкт-Петербург',
            'phone': '+7-555-888-8888',
            'email': 'spb@geekshop.ru',
            'address': 'В пределах КАД'
        },
        {
            'city': 'Нижний Новгород',
            'phone': '+7-831-777-8888',
            'email': 'nn@geekshop.ru',
            'address': 'В пределах центра'
        }
    ]
    context = {
        # 'page_title': 'контакты'.title()  # НЕ ДЕЛАТЬ ТАК (нарушение принципов MVC)
        'page_title': 'контакты',
        'locations': locations  # тестим случай с отсутствием locations (условие if)
    }
    return render(request, 'mainapp/contact.html', context)
