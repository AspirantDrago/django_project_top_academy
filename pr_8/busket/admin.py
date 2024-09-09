from django.contrib import admin
from django.db import models

from busket.models import Busket, BusketProducts
from products.models import Products

# Register your models here.
class ProductsInline(admin.TabularInline):
    model = BusketProducts


class BusketAdmin(admin.ModelAdmin):
    fields  = ['completed', 'salesman', 'customer']
    inlines = [ProductsInline]


admin.site.register(Busket, BusketAdmin)
