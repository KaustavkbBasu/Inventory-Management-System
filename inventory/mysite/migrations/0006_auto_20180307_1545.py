# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_inventory_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='id',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='productId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
