from django.shortcuts import render, redirect
from .forms import ProductoForm, CLienteForm, VentaForm
from .models import Producto, Cliente, Venta, VentaProducto


# Create your views here.

def products(request):
    producto = Producto.objects.all()
    contexto = {
        'producto': producto
    }
    print(producto)
    return render(request, 'Inventory/products.html', contexto)


def CreateProduct(request):
    form = ProductoForm()
    contexto = {
        'form': form
    }

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Products')

    return render(request, 'Inventory/CreateProduct.html', contexto)


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
    cliente = Cliente.objects.all()
    contexto = {
        'cliente': cliente
    }
    print(cliente)
    return render(request, 'Inventory/customers.html', contexto)


def CreateCustomer(request):
    form = CLienteForm
    contexto = {
        'form': form
    }

    if request.method == 'POST':
        form = CLienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Customers')

    return render(request, 'Inventory/CreateCustomer.html', contexto)


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
    contexto = {
        'venta': venta,
    }
    print(venta)
    return render(request, 'Inventory/sales.html', contexto)


def CreateSale(request):
    form = VentaForm
    contexto = {
        'form': form
    }

    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Sales')

    return render(request, 'Inventory/CreateSale.html', contexto)


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


