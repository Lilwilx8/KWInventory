from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView, View

from .forms import ProductoForm, CLienteForm, VentaForm
from .models import Producto, Cliente, Venta


# Create your views here.

class Products(View):
    model = Producto
    form_class = ProductoForm
    template_name = 'Inventory/products.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class AddProduct(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Inventory/addProduct.html'
    success_url = reverse_lazy('Products')


class UpdateProduct(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Inventory/updateProduct.html'
    success_url = reverse_lazy('Products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context


class DeleteProduct(DeleteView):
    model = Producto

    def post(self, request, pk, *args, **kwargs):
        object = Producto.objects.get(IdProducto=pk)
        object.delete()
        return redirect('Products')


class Customers(View):
    model = Cliente
    form_class = CLienteForm
    template_name = 'Inventory/customers.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['clientes'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class AddCustomer(CreateView):
    model = Cliente
    form_class = CLienteForm
    template_name = 'Inventory/addCustomer.html'
    success_url = reverse_lazy('Customers')


class UpdateCustomer(UpdateView):
    model = Cliente
    form_class = CLienteForm
    template_name = 'Inventory/updateCustomer.html'
    success_url = reverse_lazy('Customers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Producto.objects.all()
        return context


class DeleteCustomer(DeleteView):
    model = Cliente

    def post(self, request, pk, *args, **kwargs):
        object = Cliente.objects.get(IdCliente=pk)
        object.delete()
        return redirect('Customers')


class Sales(View):
    model = Venta
    form_class = VentaForm
    template_name = 'Inventory/sales.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['ventas'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class AddSale(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Inventory/addSale.html'
    success_url = reverse_lazy('Sales')


class UpdateSale(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Inventory/updateSale.html'
    success_url = reverse_lazy('Sales')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ventas'] = Producto.objects.all()
        return context


class DeleteSale(DeleteView):
    model = Venta

    def post(self, request, pk, *args, **kwargs):
        object = Venta.objects.get(IdVenta=pk)
        object.delete()
        return redirect('Sales')
