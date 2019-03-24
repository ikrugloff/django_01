from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'page_title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)  # / в начале не ставится, т.к. адрес относительный корня
    # для шаблонов


def products(request):
    context = {
        'page_title': 'каталог'
    }
    return render(request, 'mainapp/products.html', context)


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
            'city': 'Владивосток',
            'phone': '+7-333-888-8888',
            'email': 'fareast@geekshop.ru',
            'address': 'В пределах центра'
        }
    ]
    context = {
        # 'page_title': 'контакты'.title()  # НЕ ДЕЛАТЬ ТАК (нарушение принципов MVC)
        'page_title': 'контакты',
        'locations': locations  # тестим случай с отсутствием locations (условие if)
    }
    return render(request, 'mainapp/contact.html', context)
