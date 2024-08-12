from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='history'),
    path('create', create, name='history_create'),

]