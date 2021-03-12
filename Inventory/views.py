from django.shortcuts import render, redirect
from django.views import View

from .forms import ProductoForm, CLienteForm, VentaForm
from .models import Producto, Cliente, Venta, VentaProducto


# Create your views here.
#
# class products(View):
#     model = Producto
#     form_clas = ProductoForm
#     template_name = 'Inventory/products.html'
#
#     def get_queryset(self):
#         return self.model.objects.first(estado = True)
#
#     def get_context_data(self, **kwargs):
#         contexto = {}
#         contexto['productos'] = self.get_queryset()
#         contexto['from'] = self.form_clas
#         return contexto
#
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, self.get_context_data())
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_clas(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Products')
#         else:
#             form = self.form_clas()
#             return render(request, self.template_name, self.get_context_data())



def products(request):
    producto = Producto.objects.all()
    form = ProductoForm()
    contexto = {
        'form': form,
        'producto': producto
    }
    print(producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Products')
    return render(request, 'Inventory/products.html', contexto)


def EditProduct(request, Id):
    producto = Producto.objects.get(IdProducto=Id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)

        contexto = {
            'form': form
        }
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Products')

    return render(request, 'Inventory/EditProduct.html', contexto)


def DeleteProduct(request, Id):
    producto = Producto.objects.get(IdProducto=Id)
    producto.delete()
    return redirect('Products')


def customers(request):
    form = CLienteForm
    cliente = Cliente.objects.all()
    contexto = {
        'cliente': cliente,
        'form': form
    }
    if request.method == 'POST':
        form = CLienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Customers')
    print(cliente)
    return render(request, 'Inventory/customers.html', contexto)

def EditCustomer(request, Id):
    cliente = Cliente.objects.get(IdCliente=Id)
    if request.method == 'GET':
        form = CLienteForm(instance=cliente)
        contexto = {
            'form': form
        }
    else:
        form = CLienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('Customers')

    return render(request, 'Inventory/EditCustomer.html', contexto)


def DeleteCustomer(request, Id):
    cliente = Cliente.objects.get(IdCliente=Id)
    cliente.delete()
    return redirect('Customers')


def sales(request):
    venta = Venta.objects.all()
    form = VentaForm
    contexto = {
        'venta': venta,
        'form': form
    }
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Sales')
    print(venta)
    return render(request, 'Inventory/sales.html', contexto)


def EditSale(request, Id):
    venta = Venta.objects.get(IdVenta=Id)
    if request.method == 'GET':
        form = VentaForm(instance=venta)
        contexto = {
            'form': form
        }
    else:
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('Sales')

    return render(request, 'Inventory/EditSale.html', contexto)


def DeleteSale(request, Id):
    venta = Venta.objects.get(IdVenta=Id)
    venta.delete()
    return redirect('Sales')


