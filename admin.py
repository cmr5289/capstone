# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from capstone import models

# Register your models here.


class PersonEntryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class InventoryTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', )
    list_filter = ('active', )


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', )
    list_filter = ('available',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', )


class DVDAdmin(admin.ModelAdmin):
    list_display = ('title', 'actors', )


admin.site.register(models.PersonEntry, PersonEntryAdmin)
admin.site.register(models.InventoryType, InventoryTypeAdmin)
admin.site.register(models.InventoryItem, InventoryAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Dvd, DVDAdmin)
