
from django.urls import path

from . import views
app_name = "stock"

urlpatterns = [
    path('', views.index, name="index"),
    path('paginaprincipal.html', views.inicio, name="Paginagprincipal"),
    path('productos_list.html', views.productos, name="productos"),
    path('productos_delete.html', views.checkout, name="Checkout"),
    path('productos_add.html', views.agregar, name="Checkin"),
    #path('productos_search.html', views.buscar, name='Buscar'),

    ]