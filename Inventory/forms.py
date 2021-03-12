from django import forms
from .models import Producto, Cliente, Venta


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class CLienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
