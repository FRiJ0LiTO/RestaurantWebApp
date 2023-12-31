from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    # queryset se usa para filtrar los datos que se van a mostrar en la vista
    # En este caso, se hace referencia al modelo Item
    queryset = Item.objects.get_queryset()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Accedemos al contexto de la vista padre (ListView)
        # y agregamos un diccionario con los datos que tiene el modelo Item
        context = super().get_context_data(**kwargs)
        context["meals_types"] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    # model se refiere al modelo que se va a usar para mostrar los detalles
    model = Item
    template_name = 'menu_item_detail.html'
