from django import forms

from .models import RestaurantsLocations
from .validators import validate_category


class RestaurantCreateForm(forms.Form):
    name = forms.CharField(max_length=120)
    locations = forms.CharField(required=False)
    category = forms.CharField(required=False)


class RestaurantsLocationsCreateForm(forms.ModelForm):
    category = forms.CharField(validators=[validate_category], required=False)

    class Meta:
        model = RestaurantsLocations
        fields = [
            'name',
            'locations',
            'category'
        ]