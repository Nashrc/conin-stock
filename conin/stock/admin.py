from django.contrib import admin

from stock.models import productos, movimientos

admin.site.register(productos)
admin.site.register(movimientos)
