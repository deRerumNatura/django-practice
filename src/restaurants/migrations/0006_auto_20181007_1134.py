# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-07 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restaurantslocations_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantslocations',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='restaurantslocations',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]