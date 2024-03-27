from django.shortcuts import render
from .models import Producto

# Create your views here.
#CRUD solo vamos a usar C de Create

def crear_producto(request):
    
#Vamos a asignarle esos datos como valores a la nueva instancia de Producto(estatico, no es dinamico)
    producto = Producto.objects.create(
        nombre = 'Auriculares Sonny',
        descripcion = 'Los mejores del mercado',
        precio = 150000 
    )
    return render(request, 'productos.html', {'producto' : producto})