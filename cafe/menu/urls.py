from django.urls import path
from menu import views as views_menu

menu_urlpatterns = ([
    path('', views_menu.menu_list, name='menu_list'),
], 'menu')