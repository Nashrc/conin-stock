from django import forms
from stock.models import productos, movimientos

class productosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = [
            'id_prod',
            'producto',
            'cantidad',
            'vencimiento',
            'observacion',
]

        labels = {
            'id_prod' : 'Id_prod',
            'producto': 'Producto',
            'cantidad' : 'Cantidad',
            'vencimiento' : 'Vencimiento',
            'observacion' : 'Observacion',
        }

        widgets = {
            'id_prod' : forms.TextInput(attrs={'class':'form-control'}),
            'producto' : forms.TextInput(attrs={'class':'form-control'}),
            'cantidad' : forms.TextInput(attrs={'class':'form-control'}),
            'vencimiento' :forms.TextInput(attrs={'class':'form-control'}),
            'observacion' :forms.TextInput(attrs={'class':'form-control'}),
        }


#------------------------prueba falla error--------------------

class prod_outForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = [
            'id_prod',
            'producto',
            'suma',
            'resta',
            'vencimiento',
            'observacion',
]

        labels = {
            'id_prod' : 'Id_prod',
            'producto': 'Producto',
            'suma' : 'Ingreso',
            'resta' : 'Salida',
            'vencimiento' : 'Vencimiento',
            'observacion' : 'Observacion',
        }

        widgets = {
            'id_prod' : forms.TextInput(attrs={'class':'form-control'}),
            'producto' : forms.TextInput(attrs={'class':'form-control'}),
            'suma' : forms.TextInput(attrs={'class':'form-control'}),
            'resta' : forms.TextInput(attrs={'class':'form-control'}),
            'vencimiento' :forms.TextInput(attrs={'class':'form-control'}),
            'observacion' :forms.TextInput(attrs={'class':'form-control'}),
        }


#------------------------prueba falla error--------------------


class movimientosForm(forms.ModelForm):
    class Meta:
        model = movimientos
        fields = [
            'id_mov',
            'egreso',
            'ingreso',
            'fecha',
            'motivo',
            'prod_id',
        ]

        labels = {
            'id_mov' : 'Id_mov',
            'egreso': 'Egreso',
            'ingreso' : 'Ingreso',
            'fecha' : 'Fecha',
            'motivo' : 'Motivo',
            'prod_id' : 'Prod_id',
        }

        widgets = {
            'id_mov' : forms.TextInput(attrs={'class':'form-control'}),
            'egreso' : forms.TextInput(attrs={'class':'form-control'}),
            'ingreso' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha' :forms.TextInput(attrs={'class':'form-control'}),
            'motivo' :forms.TextInput(attrs={'class':'form-control'}),
            'prod_id' :forms.TextInput(attrs={'class':'form-control'}),
        }