from django.contrib import admin
from Inventory.models import Categoria, Marca, Estado, Producto, Cliente
# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Estado)
admin.site.register(Cliente)




