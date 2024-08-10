from django.shortcuts import render
from menu.models import Menu

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu/menu_list.html', {'menus':menus})
