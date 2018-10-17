from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL
# Create your models here.


class RestaurantsLocationsQuerySet(models.query.QuerySet):
    def search(self, query):
        return self.filter(
            Q(name__icontains=query)|
            Q(locations__icontains=query)|
            Q(category__icontains=query)|
            Q(item__name__icontains=query)|
            Q(item__contents__icontains=query)
        ).distinct()


class RestaurantsLocationsManager(models.Manager):
    def get_queryset(self):
        return RestaurantsLocationsQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class RestaurantsLocations(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    locations = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    objects = RestaurantsLocationsManager()

    def __str__(self):
        # for show name table in DB
        return self.name

    def get_absolute_url(self):
        return reverse("restaurants:detail", kwargs={'slug':self.slug})

    @property
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
