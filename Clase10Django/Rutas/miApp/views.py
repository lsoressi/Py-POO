from django.shortcuts import render
from .models import Usuario
from django.http import JsonResponse

# CRUD.
# c- create
# R- Read
# U- Update
# D- Delete


# CREATE
def crear_usuario(request,nombre, apellido, edad):
        nuevo_usuario = Usuario.objects.create(
                nombre = nombre,
                apellido = apellido,
                edad = edad
                
        )
        return render (request, 'usuarios.html' , {'nuevo_usuario': nuevo_usuario})

# READ

# Mostrar todos los usuarios

def mostrar_usuarios(request):
        usuarios = Usuario.objects.all()
        return render (request, 'lista_usuarios.html', {'usuarios': usuarios})

# Mostrar usuarios con filtro

def filtrar_usuarios_edad(request, edad):
        userFiltrado = Usuario.objects.filter(edad = edad)
        return render (request, 'filtrar_usuarios.html', {'userFiltrado': userFiltrado})

#UPDATE 
def update_usuario_id(request,id):
        userActualizado = Usuario.objects.get( id = id)
        userActualizado.nombre = 'Olivia'
        userActualizado.apellido = 'Olmos Soressi'
        userActualizado.edad = 15
        userActualizado.save()

        return render (request, 'user_actualizado.html', {'userActualizado' : userActualizado})

#DELETE
# Delete todos los usuarios

def delete_todos_usuarios(request):
        usuarios = Usuario.objects.all()
        usuarios.delete()
        return render (request, 'eliminar_todos.html')


# Delete un usuario por id
def delete_usuario_id(request,id):
        userEliminado = Usuario.objects.get(id = id)
        userEliminado.delete()
        usuarios = Usuario.objects.all()
        return render (request,'user_eliminado.html',{'id_Eliminado': id,'usuarios': usuarios})

#JSON: permite pasar datos de manera muy liviana (java script object....)
#Crear un diccionario con datos que quieres devolver en formato json
def ejemplo_jason_view1(request):
        data = {'mensaje': 'Hola desde JsonResponse!', 'numero': 42}
        return JsonResponse(data)

#Es un html que se ve en formato json
def ejemplo_jason_views2(request):
        data = list(Usuario.objects.values('nombre', 'apellido', 'edad'))
        return render (request, 'json.html', {'data': data})




 