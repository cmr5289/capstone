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
        verbose_name="Employee Number",
        max_length=9,
        blank=False,
        null=False)
    # Phone Number
    phone_number = models.CharField(
        max_length=14,
        verbose_name="Phone Number",
        blank=True,
        null=True)
    # Employee Role
    role = models.CharField(
        max_length=100,
        verbose_name="Employee Role",
        blank=False,
        null=False)
    # Email
    email = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    # Department
    department = models.CharField(
        max_length=255,
        blank=True,
        null=True)
    # Active
    active = models.BooleanField()

    def get_first_name(self):
        return self.name.split(" ")[0]

    def get_last_name(self):
        temp = self.name.split(" ")
        return temp[len(temp) - 1]


class InventoryType(models.Model):
    # Type Id
    type_id = models.AutoField(
        primary_key=True)
    # Type Name
    type_name = models.CharField(
        max_length=100,
        verbose_name="Type Name",
        null=False,
        blank=False)
    active = models.BooleanField()

    def __str__(self):
        return "%s" % (self.type_name)

    def __unicode__(self):
        return "%s" % (self.type_name)


class InventoryItem(models.Model):
    # Inventory Role
    inventory_id = models.AutoField(
        primary_key=True)
    # Available
    available = models.BooleanField()
    # Active
    active = models.BooleanField()
    # Price
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    # Inventory Type
    inventory_type = models.ForeignKey(
        InventoryType,
        null=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'active': True})

    def __str__(self):
        return "%s" % (
            str(self.inventory_id) + " " + self.inventory_type.type_name
        )

    def __unicode__(self):
        return "%s" % (
            str(self.inventory_id) + " " + self.inventory_type.type_name
        )


class Book(models.Model):
    # Book Id
    book_id = models.AutoField(
        primary_key=True)
    # Title
    title = models.CharField(
        max_length=200,
        verbose_name="Book Title",
        null=False,
        blank=False)
    # Author
    author = models.CharField(
        max_length=200,
        verbose_name="Author",
        null=False,
        blank=False)
    # Publisher
    publisher = models.CharField(
        max_length=200,
        verbose_name="Publisher",
        null=False,
        blank=False)
    # Copyright Date
    copyright_date = models.DateField(
        verbose_name="Copyright Date")
    # Description
    description = models.TextField(
        null=True,
        blank=True)
    # ISBN
    isbn = models.IntegerField(
        verbose_name="ISBN",
        null=True,
        blank=True)
    # Publication Date
    publication_date = models.DateField(
        verbose_name="Publication Date")
    # Series
    series = models.CharField(
        max_length=200,
        verbose_name="Series Name",
        null=True,
        blank=True)
    # Number of Pages
    pages = models.IntegerField(
        null=True,
        blank=True)
    # Inventory ID
    inventory = models.OneToOneField(
        InventoryItem,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)


class Dvd(models.Model):
    # DVD Id
    dvd_id = models.AutoField(
        primary_key=True)
    # Title
    title = models.CharField(
        max_length=200,
        verbose_name="DVD Title",
        null=False,
        blank=False)
    # Actors
    actors = models.CharField(
        max_length=200,
        verbose_name="Actors",
        null=True,
        blank=True)
    # Publisher
    run_time = models.CharField(
        max_length=200,
        verbose_name="Run Time",
        null=True,
        blank=True)
    # Raiting
    raiting = models.CharField(
        max_length=10,
        verbose_name="Raiting",
        null=False,
        blank=False)
    # Description
    description = models.TextField(
        null=True,
        blank=True)
    # Release Date
    release_date = models.DateField(
        verbose_name="Publication Date")
    # Inventory ID
    inventory = models.OneToOneField(
        InventoryItem,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
