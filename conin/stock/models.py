from django.db import models



class productos(models.Model):
	id_prod = models.IntegerField(primary_key=True,)
	producto = models.CharField(max_length=100)
	cantidad = models.IntegerField()
	vencimiento = models.CharField(max_length=10)
	observacion = models.CharField(max_length=100)
	resta = models.IntegerField(default=0)
	suma = models.IntegerField(default=0)
	#total =models.IntegerField()

	#def edit(request,id_prod):
	#	cant = 




class movimientos(models.Model):
	id_mov = models.IntegerField(primary_key=True,)
	egreso = models.IntegerField()
	ingreso = models.IntegerField()
	fecha = models.CharField(max_length=10)
	motivo = models.CharField(max_length=100)
	prod_id = models.IntegerField()



#producto.objects.filter(id=id_producto_a_eliminar.delete)