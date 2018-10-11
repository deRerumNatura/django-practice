from django.conf.urls import url, include

from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemCreateView,
)

urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='detail'),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
]

