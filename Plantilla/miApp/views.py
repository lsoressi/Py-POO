from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

plantilla = """
        <html>
        <body>
        <h1> Hola Mundo </h1>
        </body>
        <html>
"""

#Pensemos una lista de diccionarios


def saludar(request):

    cursos_realizados = [
        {'titulo': 'HTML Y CSS', 'descripcion': 'Bases para el maquetado'},
        {'titulo': 'Javascript', 'descripcion': 'Esencial para una web dinamica'},
        {'titulo': 'SQL', 'descripcion': 'Mi primer base de datos'},
    ]
    
    nombre = 'Luciana'
    ruta = "C:/Users/User/Desktop/Py-POO/Plantilla/miApp/Templates/saludo.html"
    doc_externo = open(ruta)
    nombre = 'Luciana'
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'nombre_usuario' : nombre, 'cursos': cursos_realizados})  #el lugar donde almacenamos los datos que va a usar la plantilla
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


