# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 07:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='productId',
        ),
    ]
