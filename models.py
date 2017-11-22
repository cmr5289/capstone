# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class PersonEntry(models.Model):
    # Name
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    # Employee Number
    employee_number = models.CharField(
        max_length=50,
        verbose_name="Employee Number",
        blank=True,
        null=True)

    def get_first_name(self):
        return self.name.split(" ")[0]

    def get_last_name(self):
        temp = self.name.split(" ")
        return temp[len(temp) - 1]
