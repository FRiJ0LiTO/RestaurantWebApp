from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuList(generic.ListView):
    # queryset se usa para filtrar los datos que se van a mostrar en la vista
    # En este caso, se hace referencia al modelo Item
    queryset = Item.objects.order_by('-date_created')
    template_name = 'index.html'


class MenuItemDetail(generic.DetailView):
    # model se refiere al modelo que se va a usar para mostrar los detalles
    model = Item
    template_name = 'menu_item_detail.html'
