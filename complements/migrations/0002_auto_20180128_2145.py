# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-28 18:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='attribute_limited',
            new_name='attribute_is_limited',
        ),
    ]
