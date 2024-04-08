from django.contrib import admin
from .models import Producto, Proveedor


# Register your models here.
# Inscribir el modelo en el gestor del admin para poder usarlo desde ahi


#modelAdmin
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['rSocial', 'domicilio', 'cuit']

    #crear un imput de busqueda o sea filtrar
    search_fields = ['rSocial']

admin.site.register(Proveedor, ProveedorAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock_actual', 'proveedor']

    #crear un imput de busqueda o sea filtrar
    search_fields = ['nombre']

admin.site.register(Producto, ProductoAdmin)



