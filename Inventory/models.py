from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Categoria(models.Model):
    IdCategoria = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50, null=False, verbose_name='Nombre Categoria')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.Nombre


class Marca(models.Model):
    IdMarca = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.Nombre


class Estado(models.Model):
    IdEstado = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.Nombre


class Producto(models.Model):
    IdProducto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    Precio = models.IntegerField(null=False)
    Stock = models.IntegerField(null=False)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=False)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False)
    Gramage = models.CharField(max_length=30, null=False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['Nombre']

    def __str__(self):
        return self.Nombre


class Cliente(models.Model):
    IdCliente = models.AutoField(primary_key=True)
    Documento = models.IntegerField(null=False)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['Nombre']

    def __str__(self):
        return self.Nombre

class Venta(models.Model):
    IdVenta = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    Fecha = models.DateTimeField(auto_now_add=True)
    Valor = models.IntegerField()

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return str(self.IdVenta)

class VentaProducto(models.Model):
    Venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(default=1)

    def __str__(self):
        return str(self.Venta)

class Roles(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Nombre)





