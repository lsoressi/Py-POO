from django.shortcuts import render
from .models import Estudiante



# Crear un estudiante
def crear_Estudiante(request,nombre, apellido, edad, nota):
        nuevo_estudiante = Estudiante.objects.create(
                nombre = nombre,
                apellido = apellido,
                edad = edad,
                nota = nota         
        )
        return render (request, 'crear_Estudiante.html' , {'nuevo_estudiante': nuevo_estudiante})


# READ

# Mostrar todos los estudiantes

def mostrar_Estudiantes(request):
        estudiantes = Estudiante.objects.all()
        return render (request, 'lista_Estudiantes.html', {'estudiantes': estudiantes})

# Mostrar estudiantes con filtro

def filtrar_estudiante_edad(request, edad):
        
        estudianteFiltrado = Estudiante.objects.filter(edad__gte = edad)
        return render (request, 'estudiante_Filtro.html', {'estudianteFiltrado': estudianteFiltrado, 'edad': edad})
        

        #estudiantes = Estudiante.objects.all()
        #for estudiante in estudiantes:
                #if estudiante.edad > edad:
                        #estudianteFiltrados = estudiante
        


#Actualizar la nota de un estudiante

def actualizar_nota_id(request,id):
        notaActualizada = Estudiante.objects.get( id = id)
        notaActualizada.nombre = 'Angela'
        notaActualizada.apellido = 'Olmos'
        notaActualizada.nota= '6'
        notaActualizada.save()

        return render (request, 'nota_Actualizada.html', {'notaActualizada' : notaActualizada})

# Delete a un estudiante por id

def eliminar_estudiante_id(request,id):
        estudianteEliminado = Estudiante.objects.get(id = id)
        estudianteEliminado.delete()
        usuarios = Estudiante.objects.all()
        return render (request,'estudiante_Eliminado.html',{'id_Eliminado': id,'estudiante': Estudiante})