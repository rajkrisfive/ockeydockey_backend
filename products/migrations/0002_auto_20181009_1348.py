# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-09 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('created',), 'verbose_name': 'SubCategory', 'verbose_name_plural': 'SubCategories'},
        ),
    ]
