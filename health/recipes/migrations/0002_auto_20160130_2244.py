# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
        migrations.AddField(
            model_name='recipe',
            name='imageUrl',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
