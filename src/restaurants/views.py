from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import RestaurantsLocations
from .forms import RestaurantsLocationsCreateForm
# Create your views(controllers) here.


def restaurant_createview(request):
    form = RestaurantsLocationsCreateForm(request.POST or None)
    errors = None

    if form.is_valid():
        form.save()

        return HttpResponseRedirect("/restaurants/")
    else:
        errors = form.errors

    template_name = "restaurants/form.html"
    context = {"form": form, "errors": errors}

    return render(request, template_name, context)


def restaurants_list(request):
    template_name = "restaurants/restaurantslocations_list.html"
    queryset = RestaurantsLocations.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, template_name, context)


# return all records
class RestaurantListView(ListView):
    def get_queryset(self):
        if self.kwargs.get('slug'):
            return RestaurantsLocations.objects.filter(category__icontains=self.kwargs.get('slug'))

        return RestaurantsLocations.objects.all()


# return one record
class RestaurantDetailView(DetailView):
    queryset = RestaurantsLocations.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return  context


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantsLocationsCreateForm
    template_name = "restaurants/form.html"
    success_url = '/restaurants/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user

        return super(RestaurantCreateView, self).form_valid(form)


