from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.http import Http404
from django.views.generic import DetailView, View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import pb
from restaurants.models import RestaurantsLocations
from menus.models import Item
from profiles.models import Profile
from .forms import RegisterForm

User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = "/"

class ProfileFollowToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user_to_toggle = request.POST.get("username")
        profile_, is_following = Profile.objects.toggle_follow(request.user, user_to_toggle)
        return redirect(f"/profiles/{profile_.user.username}/")


class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            return Http404

        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)

        user = self.get_object()
        query = self.request.GET.get('q')
        items_exist = Item.objects.filter(user=user).exists()
        qs = RestaurantsLocations.objects.filter(owner=user)

        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following

        if query:
            qs = qs.search(query)

        if qs.exists() and items_exist:
            context['locations'] = qs

        return context
