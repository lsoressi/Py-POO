from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse


# Create your views here.
def mostrar_Template(request):
    ruta = 'C:/Users/User/Desktop/Py-POO/StaticFiles/miApp/Templates/Index.html'
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    return HttpResponse(plantilla.render(contexto))

