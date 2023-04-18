from django.shortcuts import render
from .models import New



def home(request):
    data = {
        'news': New.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'zzz/home.html', data)

def contacts(request):
    return render(request, 'zzz/contacts.html', {'title': 'Страничка про Что то'})

def aegis(request):
    return render(request, 'zzz/aegis.html', {'title': 'Страничка про дудку'})

def parad(request):
    return render(request, 'zzz/parad.html', {'title': 'фото парада'})