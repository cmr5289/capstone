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
    employee_number = models.IntegerField(
        verbose_name="Employee Number",
        blank=False,
        null=False)
    # Phone Number
    phone_number = models.CharField(
        max_length=20,
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


class Inventory(models.Model):
    # Inventory Role
    inventory_id = models.AutoField(
        primary_key=True)
    # Available
    available = models.BooleanField()
    # Inventory Type
    inventory_type = models.ForeignKey(
        InventoryType,
        null=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'active': True})


class Books(models.Model):
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
    description = models.TextField()
    # ISBN
    isbn = models.IntegerField(
        verbose_name="ISBN")
    # Publication Date
    publication_date = models.DateField(
        verbose_name="Publication Date")
    # Series
    series = models.CharField(
        max_length=200,
        verbose_name="Series Name",
        null=False,
        blank=False)
    # Number of Pages
    pages = models.IntegerField()
    # Inventory ID
    inventory = models.ForeignKey(
        Inventory,
        null=True,
        on_delete=models.SET_NULL)


class Dvd(models.Model):
    # DVD Id
    dvd_id = models.AutoField(
        primary_key=True)
    # Title
    title = models.CharField(
        max_length=200,
        verbose_name="Book Title",
        null=False,
        blank=False)
    # Actors
    actors = models.CharField(
        max_length=200,
        verbose_name="Actores",
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
    # Release Date
    release_date = models.DateField(
        verbose_name="Publication Date")
    # Inventory ID
    inventory = models.ForeignKey(
        Inventory,
        null=True,
        on_delete=models.SET_NULL)
