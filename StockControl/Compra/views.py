from django.shortcuts import render
from .models import Proveedor
from .forms import proveedor_Formulario
from .models import Producto
from .forms import producto_Formulario



# Create your views here.
def crear_proveedor(request):
        
        data = {
                'form': proveedor_Formulario()
        }

        if request.method=='POST':
                formulario = proveedor_Formulario(data=request.POST)
                if formulario.is_valid():
                        formulario.save()
                        data['mensaje'] = 'Proveedor Guardado'
                else:
                        data['form'] = formulario

        return render (request, 'crear_Proveedor.html', data)


# READ

# Mostrar todos los proveedores

def mostrar_Proveedores(request):
        proveedores = Proveedor.objects.all()
        return render (request, 'lista_Proveedores.html', {'proveedores': proveedores})




def crear_producto(request):
        
        data = {
                'form': producto_Formulario()
        }

        if request.method=='POST':
                formulario = producto_Formulario(data=request.POST)
                if formulario.is_valid():
                        formulario.save()
                        data['mensaje'] = 'Producto Guardado'
                else:
                        data['form'] = formulario

        return render (request, 'crear_Producto.html', data)


# READ

# Mostrar todos los productos

def mostrar_Producto(request):
        productos = Producto.objects.all()
        return render (request, 'lista_Productos.html', {'productos': productos})