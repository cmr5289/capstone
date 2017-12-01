# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.urls import reverse

import re

from models import InventoryItem, Dvd, Book, PersonEntry, InventoryType
from forms import EmployeeEditForm, BookEditForm, DVDEditForm

from django.shortcuts import redirect

# Create your views here.


@login_required()
def home(request):
    """
    homepage for portfolio
    """
    responseData = {
    }

    return render(
        request,
        "capstone/home.html",
        responseData
    )


@login_required()
def inventory(request):
    """
    Page to view all inventory
    """

    inventory_items = InventoryItem.objects.filter(
        active=True
    )

    for item in inventory_items:
        if item.inventory_type.type_name.lower() == "book":
            item.details = Book.objects.filter(
                inventory__inventory_id=item.pk
            ).first()
        elif item.inventory_type.type_name.lower() == "dvd":
            item.details = Dvd.objects.filter(
                inventory__inventory_id=item.pk
            ).first()
        else:
            item.details = {}

    responseData = {
        "inventory_items": inventory_items,
    }

    return render(
        request,
        "capstone/inventory.html",
        responseData
    )


@login_required()
def inventory_details(request, pk):
    """
    Inventory Item details page
    """
    template = ""
    inventory_item = get_object_or_404(InventoryItem, inventory_id=pk)

    if inventory_item.inventory_type.type_name.lower() == "book":
        inventory_item.details = Book.objects.filter(
            inventory__inventory_id=inventory_item.pk
        ).first()
        template = "capstone/book_details.html"
    elif inventory_item.inventory_type.type_name.lower() == "dvd":
        inventory_item.details = Dvd.objects.filter(
            inventory__inventory_id=inventory_item.pk
        ).first()
        template = "capstone/dvd_details.html"
    else:
        inventory_item.details = {}

    responseData = {
        "inventory_item": inventory_item,
    }

    return render(
        request,
        template,
        responseData
    )


@login_required()
def inventory_edit(request, pk):
    """
    Inventory Edit Page
    """
    template = ""
    inventory_item = get_object_or_404(InventoryItem, inventory_id=pk)

    if inventory_item.inventory_type.type_name.lower() == "book":
        inventory_item.details = Book.objects.filter(
            inventory__inventory_id=inventory_item.pk
        ).first()
        template = "capstone/book_edit.html"
    elif inventory_item.inventory_type.type_name.lower() == "dvd":
        inventory_item.details = Dvd.objects.filter(
            inventory__inventory_id=inventory_item.pk
        ).first()
        template = "capstone/dvd_edit.html"
    else:
        inventory_item.details = {}

    if request.method == 'POST':
        if inventory_item.inventory_type.type_name.lower() == "book":
            form = BookEditForm(request.POST, instance=inventory_item.details)
        elif inventory_item.inventory_type.type_name.lower() == "dvd":
            form = DVDEditForm(request.POST, instance=inventory_item.details)
        else:
            form = {}

        if form.is_valid():
            inventory_item.details = form.save(commit=False)

            inventory_item.price = form.cleaned_data['price']

            inventory_item.save()
            inventory.details.save()

            return redirect(
                'inventory_details',
                pk=inventory_item.inventory_id
            )
    else:
        if inventory_item.inventory_type.type_name.lower() == "book":
            form = BookEditForm(instance=inventory_item.details)
        elif inventory_item.inventory_type.type_name.lower() == "dvd":
            form = DVDEditForm(instance=inventory_item.details)
        else:
            form = {}

        form.fields["price"].initial = \
            inventory_item.price

    responseData = {
        "inventory_item": inventory_item,
        "form": form,
    }

    return render(
        request,
        template,
        responseData
    )


@login_required()
def inventory_new(request):
    """
    Inventory Edit Page
    """
    type = request.path.split("/")[-2]
    template = ""

    if type == "book":
        template = "capstone/book_edit.html"
    elif type == "dvd":
        template = "capstone/dvd_edit.html"
    else:
        template = ""

    if request.method == 'POST':
        if type == "book":
            form = BookEditForm(request.POST)
        elif type == "dvd":
            form = DVDEditForm(request.POST)
        else:
            form = {}

        if form.is_valid():
            new_item = form.save(commit=False)

            inventory_type = InventoryType.objects.filter(
                type_name__contains=type
            ).first()

            inventory_item = InventoryItem(
                available=True,
                active=True,
                price=form.cleaned_data['price'],
                inventory_type=inventory_type
            )

            inventory_item.save()
            new_item.save()

            new_item.inventory = inventory_item
            new_item.save()

            return redirect(
                'inventory_details',
                pk=inventory_item.inventory_id
            )
    else:
        if type == "book":
            form = BookEditForm()
        elif type == "dvd":
            form = DVDEditForm()
        else:
            form = {}

    responseData = {
        "form": form,
    }

    return render(
        request,
        template,
        responseData
    )


@login_required()
def employees(request):
    """
    Inventory Item details page
    """
    employees = PersonEntry.objects.filter(
        active=True
    )

    responseData = {
        "employees": employees,
    }

    return render(
        request,
        "capstone/employees.html",
        responseData
    )


@login_required()
def employee_details(request, pk):
    """
    Inventory Item details page
    """
    employee = get_object_or_404(PersonEntry, pk=pk)

    responseData = {
        "employee": employee,
    }

    return render(
        request,
        "capstone/employee_details.html",
        responseData
    )


@login_required()
def employee_edit(request, pk):
    """
    Inventory Item details page
    """
    employee = get_object_or_404(PersonEntry, pk=pk)

    if request.method == 'POST':
        form = EmployeeEditForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)

            scrub_phone_number = re.sub(
                r'(\(|\)|-|\ |[a-z]|[A-Z]|\.)',
                '',
                form.cleaned_data['raw_phone_number'])

            scrub_phone_number = scrub_phone_number[:3] + \
                "-" + scrub_phone_number[3:6] + \
                "-" + scrub_phone_number[6:]

            employee.phone_number = scrub_phone_number

            employee.save()

            return redirect('employee_details', pk=employee.pk)
    else:
        form = EmployeeEditForm(instance=employee)
        form.fields["raw_phone_number"].initial = \
            employee.phone_number

    responseData = {
        "employee": employee,
        "form": form,
    }

    return render(
        request,
        "capstone/employee_edit.html",
        responseData
    )


@login_required()
def employee_new(request):
    """
    Create New Employee
    """
    if request.method == 'POST':
        form = EmployeeEditForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)

            scrub_phone_number = re.sub(
                r'(\(|\)|-|\ |[a-z]|[A-Z]|\.)',
                '',
                form.cleaned_data['raw_phone_number'])

            scrub_phone_number = scrub_phone_number[:3] + \
                "-" + scrub_phone_number[3:6] + \
                "-" + scrub_phone_number[6:]

            employee.phone_number = scrub_phone_number

            employee.active = True

            employee.save()

            return redirect('employee_details', pk=employee.pk)
    else:
        form = EmployeeEditForm()

    responseData = {
        "form": form,
    }

    return render(
        request,
        "capstone/employee_edit.html",
        responseData
    )
