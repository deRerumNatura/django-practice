from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from restaurants.models import RestaurantsLocations


class Item(models.Model):
    # todo спросить по поводу что можно делать в модели. И как это взаимодействует с темплейтами
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(RestaurantsLocations)

    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='separate items by comma')
    excludes = models.TextField(blank=True, null=True, help_text='separate items by comma')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        # for show name table in DB
        return self.name

    def get_contents(self):
        return self.contents.split(',')

    def get_excludes(self):
        return self.excludes.split(',')

    def get_absolute_url(self):
        return reverse("items:detail", kwargs={'pk': self.pk})
