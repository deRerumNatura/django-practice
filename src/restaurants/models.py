from django.db import models


# Create your models here.
class RestaurantsLocations(models.Model):
    name = models.CharField(max_length=120)
    locations = models.CharField(max_length=120, null=True, blank=True)
