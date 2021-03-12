from django.shortcuts import render, redirect
from .forms import ProductoForm, CLienteForm
from .models import Producto, Cliente


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
