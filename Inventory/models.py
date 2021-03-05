from django.db import models


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
