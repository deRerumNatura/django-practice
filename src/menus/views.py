from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Item
from .forms import ItemForm

class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(CreateView):
    form_class = ItemForm

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemUpdateView(UpdateView):
    form_class = ItemForm

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
