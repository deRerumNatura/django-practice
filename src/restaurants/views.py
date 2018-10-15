from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import RestaurantsLocations
from .forms import RestaurantsLocationsCreateForm


class RestaurantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        # if self.kwargs.get('slug'):
        #     return RestaurantsLocations.objects.filter(category__icontains=self.kwargs.get('slug'))
        #
        return RestaurantsLocations.objects.filter(owner=self.request.user)


# return one record
class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantsLocations.objects.filter(owner=self.request.user)

    # def get_context_data(self, *args, **kwargs):
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return  context


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantsLocationsCreateForm
    template_name = "form.html"
    success_url = "/restaurants/"

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.owner = self.request.user
    #
    #     return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        # что бы изменить как то контекст
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Add restaurant"
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantsLocationsCreateForm
    template_name = "restaurants/detail-update.html"
    success_url = "/restaurants/"

    def get_context_data(self, *args, **kwargs):
        # что бы изменить как то контекст
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = "Add restaurant"

        return context

    def get_queryset(self):
        return RestaurantsLocations.objects.filter(owner=self.request.user)


