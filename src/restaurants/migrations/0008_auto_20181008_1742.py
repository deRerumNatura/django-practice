# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-08 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_restaurantslocations_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantslocations',
            name='slug',
            field=models.SlugField(),
        ),
    ]
