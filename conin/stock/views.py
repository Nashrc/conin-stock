from django.http import HttpResponseRedirect, HttpResponse,FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import productos, movimientos
from django.http import Http404
from stock.forms import productosForm, movimientosForm, prod_outForm
from stock.models import productos as prod
#from stock.models import cantidad , suma, resta

from stock.models import productos
#from stock.productos.models import productos

def index(request):
    return render(request, 'C:/conin/stock/templates/stock/index.html')

def inicio(request):
    return render(request, 'C:/conin/stock/templates/stock/paginaprincipal.html')

def productos(request):
	resultado= prod.objects.all()
	return render(request, 'C:/conin/stock/templates/stock/productos_list.html',{"productos":resultado})
















def checkout(request):
	if request.method == 'POST':
		form = prod_outForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('stock:Paginagprincipal')
	else:
		form = prod_outForm()

	return render(request, 'C:/conin/stock/templates/stock/productos_delete.html', {'form':form})

    #return render(request, 'C:/conin/stock/templates/stock/productos_delete.html')






















def agregar(request):#productosForm
	if request.method == 'POST':
		form = productosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('stock:Paginagprincipal')
	else:
		form = productosForm()

	return render(request, 'C:/conin/stock/templates/stock/productos_add.html', {'form':form})
    #return render(request, 'C:/conin/stock/templates/stock/productos_add.html')

