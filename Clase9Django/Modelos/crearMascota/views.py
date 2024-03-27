from django.shortcuts import render
from .models import Mascota

# Create your views here.
#CRUD solo vamos a usar C de Create

def crear_mascota(request):
    
#Vamos a asignarle esos datos como valores a la nueva instancia de Producto(estatico, no es dinamico)
    mascota = Mascota.objects.create(
        nombre = 'Olivia',
        raza = 'Dachshund, marron fuego',
        edad = 15
    )

    mascota2 = Mascota.objects.create(
        nombre = 'Ciro',
        raza = 'Ovejero Aleman',
        edad = 13
    )
    return render(request, 'mascotas.html', {'mascota' : mascota, 'mascota2' : mascota2})