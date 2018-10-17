from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from menus.views import HomeView
from profiles.views import ProfileFollowToggle, RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^follow-user/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^items/', include('menus.urls', namespace='items')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
]

