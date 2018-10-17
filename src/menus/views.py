from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View

from .models import Item
from .forms import ItemForm
from .utils import pb

class HomeView(View):
    def get(self, request, *args, **kwargs): # todo что прилетает в реквесте?
        if not request.user.is_authenticated():
            return render(request, "home.html", {})

        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True) # todo как работают параметры?

        return render(request, "menus/home-feed.html", {"object_list": qs})


class ItemListView(ListView, LoginRequiredMixin):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = "form.html"
    # success_url = "/items/"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        # что бы изменить как то контекст
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Create menu item"
        return context


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ItemForm
    template_name = "form.html"
    # success_url = "/items/"

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    # def get_context_data(self, *args, **kwargs):
    #     # что бы изменить как то контекст
    #     context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
    #     context['title'] = "Update menu item"
    #     return context

    def get_form_kwargs(self):
        kwargs = super(ItemUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
