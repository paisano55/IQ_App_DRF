from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'quotemaker'

urlpatterns = [
    path('cpu/',views.cpu_list)
]
