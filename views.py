# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from models import InventoryItem, Dvd, Book, InventoryType, PersonEntry

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
    inventory_item = InventoryItem.objects.filter(
        inventory_id=pk
    ).first()

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
