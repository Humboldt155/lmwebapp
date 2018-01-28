# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-28 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complements', '0002_auto_20180128_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'ordering': ['attribute_id'], 'verbose_name': 'атрибут', 'verbose_name_plural': 'атрибуты'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['department_id'], 'verbose_name': 'отдел', 'verbose_name_plural': 'отделы'},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['link_value', 'link_attribute', 'link_model'], 'verbose_name': 'связь', 'verbose_name_plural': 'связи'},
        ),
        migrations.AlterModelOptions(
            name='lmcode',
            options={'ordering': ['lmcode_id'], 'verbose_name': 'lm код', 'verbose_name_plural': 'lm коды'},
        ),
        migrations.AlterModelOptions(
            name='model',
            options={'ordering': ['model_id'], 'verbose_name': 'модель Адео', 'verbose_name_plural': 'модели Адео'},
        ),
        migrations.AlterModelOptions(
            name='value',
            options={'ordering': ['value_id'], 'verbose_name': 'значение атрибута', 'verbose_name_plural': 'значения атрибутов'},
        ),
        migrations.AlterField(
            model_name='link',
            name='link_value',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='complements.Value'),
        ),
        migrations.AlterUniqueTogether(
            name='link',
            unique_together=set([('link_model', 'link_attribute', 'link_value')]),
        ),
    ]
