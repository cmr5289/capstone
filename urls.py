"""
URLS for portfolio
"""

from views import home, inventory, inventory_details
from django.conf.urls import *

urlpatterns = [
    url(r'^$', home, name='capstone_home'),

    url(r'^inventory/$', inventory, name='inventory'),
    url(r'^inventory/(?P<pk>\d+)/$',
        inventory_details,
        name='inventory_details'
        ),
]
