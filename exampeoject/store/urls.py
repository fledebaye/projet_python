import re

from django.urls import path, re_path
from django.conf.urls import include 
from . import views



urlpatterns = [
    path('', views.listing, name='listing'),
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    path('search/', views.search, name='search'),

    
]