from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'history'

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('<int:pk>', show, name='show'),


]