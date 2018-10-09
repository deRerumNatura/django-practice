from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator
from .validators import validate_category


# Create your models here.
class RestaurantsLocations(models.Model):
    name = models.CharField(max_length=120)
    locations = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        # for show name table in DB
        return self.name

    @property #TODO спросить
    def title(self):
        return self.name


def rf_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving...')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def rf_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved...')
#     print(instance.slug)
#     if not instance.slug: # if not is set
#         instance.slug = unique_slug_generator(instance)
#         instance.save()


pre_save.connect(rf_pre_save_receiver, sender=RestaurantsLocations)

# post_save.connect(rf_post_save_receiver, sender=RestaurantsLocations)
