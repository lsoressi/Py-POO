from django.urls import path
from . import views

urlpatterns = [

    path('crearProveedor/', views.crear_proveedor),
    path('listaProveedores/', views.mostrar_Proveedores),
    path('crearProducto/', views.crear_producto),
    path('', views.mostrar_Producto)


]