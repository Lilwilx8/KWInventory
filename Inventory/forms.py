from  django import forms
from .models import Producto, Cliente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class CLienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'