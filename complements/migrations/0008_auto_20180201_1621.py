# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-01 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complements', '0007_auto_20180201_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'ordering': ['attribute_id'], 'verbose_name': 'атрибут', 'verbose_name_plural': 'Structure_2 атрибуты'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['department_id'], 'verbose_name': 'LMRussia отдел', 'verbose_name_plural': 'LMRussia_1 отделы'},
        ),
        migrations.AlterModelOptions(
            name='departmentadeo',
            options={'ordering': ['department_adeo_id'], 'verbose_name': 'Adeo отдел', 'verbose_name_plural': 'Adeo_1 отделы'},
        ),
        migrations.AlterModelOptions(
            name='lmcode',
            options={'ordering': ['lmcode_id'], 'verbose_name': 'lm код', 'verbose_name_plural': 'Structure_4 lm коды'},
        ),
        migrations.AlterModelOptions(
            name='model',
            options={'ordering': ['model_id'], 'verbose_name': 'модель Адео', 'verbose_name_plural': 'Structure_1 модели Адео'},
        ),
        migrations.AlterModelOptions(
            name='modelgroupadeo',
            options={'ordering': ['model_group_adeo_id'], 'verbose_name': 'Adeo группа моделей', 'verbose_name_plural': 'Adeo_3 группы моделей'},
        ),
        migrations.AlterModelOptions(
            name='subdepartment',
            options={'ordering': ['sub_department_id'], 'verbose_name': 'LMRussia подотдел', 'verbose_name_plural': 'LMRussia_2 потделы'},
        ),
        migrations.AlterModelOptions(
            name='subdepartmentadeo',
            options={'ordering': ['sub_department_adeo_id'], 'verbose_name': 'Adeo подотдел', 'verbose_name_plural': 'Adeo_2 потделы'},
        ),
        migrations.AlterModelOptions(
            name='value',
            options={'ordering': ['value_id'], 'verbose_name': 'значение атрибута', 'verbose_name_plural': 'Structure_3 значения атрибутов'},
        ),
        migrations.RenameField(
            model_name='modelgroupadeo',
            old_name='su_department_adeo',
            new_name='sub_department_adeo',
        ),
    ]
