# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-30 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0011_auto_20171130_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personentry',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Phone Number'),
        ),
    ]
