from django.db import models
from django.conf import settings

from restaurants.models import RestaurantsLocations


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(RestaurantsLocations)
    name = models.CharField(max_length=120)
    content = models.TextField(help_text='separate items by comma')
    excludes = models.TextField(blank=True, null=True, help_text='separate items by comma')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.content.split(',')

    def get_excludes(self):
        return self.excludes.split(',')
