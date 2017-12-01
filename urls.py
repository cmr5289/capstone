"""
URLS for portfolio
"""

from views import home, inventory, inventory_details,\
    employees, employee_details, employee_edit, inventory_edit,\
    inventory_new, employee_new
from django.conf.urls import *

urlpatterns = [
    url(r'^$', home, name='capstone_home'),

    url(r'^inventory/$', inventory, name='inventory'),
    url(r'^inventory/(?P<pk>\d+)/$',
        inventory_details,
        name='inventory_details'
        ),
    url(r'^inventory/(?P<pk>\d+)/edit/$',
        inventory_edit,
        name='inventory_edit'
        ),
    url(r'^inventory/new/book/$',
        inventory_new,
        name='book_new'
        ),
    url(r'^inventory/new/dvd/$',
        inventory_new,
        name='dvd_new'
        ),
    url(r'^employees/$',
        employees,
        name='employees'
        ),
    url(r'^employees/(?P<pk>\d+)/$',
        employee_details,
        name='employee_details'
        ),
    url(r'^employees/(?P<pk>\d+)/edit/$',
        employee_edit,
        name='employee_edit'
        ),
    url(r'^employees/new/$',
        employee_new,
        name='employee_new'
        ),
]
