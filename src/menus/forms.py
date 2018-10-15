from django import forms

from .models import Item
from restaurants.models import RestaurantsLocations

from .utils import pb


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    def __init__(self, user=None, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        pb(kwargs)
        self.fields['restaurant'].queryset = RestaurantsLocations.objects.filter(owner=user)
