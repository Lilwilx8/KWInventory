from django import forms

from .models import Producto, Cliente, Venta


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                }
            ),
            'Precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio',
                }
            ),
            'Stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Stock',
                }
            ),
            'Categoria': forms.Select(
                attrs={
                    'class': 'form-select',

                    'placeholder': 'Categoria',
                }
            ),
            'Marca': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Marca',
                }
            ),
            'Estado': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Estado',
                }
            ),
            'Gramage': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Peso',
                }
            ),

        }


class CLienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                }
            ),
            'Apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                }
            ),
            'Telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Telefono',
                }
            ),
            'Documento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Documento',
                }
            ),
        }


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

        widgets = {
            'Cliente': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Cliente',
                }
            ),
            'Valor': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Total',
                }
            ),
        }
