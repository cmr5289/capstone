# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-27 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0008_auto_20171127_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvd',
            name='raiting',
            field=models.CharField(default='R', max_length=10, verbose_name='Raiting'),
            preserve_default=False,
        ),
    ]