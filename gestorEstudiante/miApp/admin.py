from django.contrib import admin
from .models import Estudiante

# Register your models here.
# Inscribir el modelo en el gestor del admin para poder usarlo desde ahi


#modelAdmin
class Estudianteadmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'domicilio','edad', 'nota']

    #crear un imput de busqueda o sea filtrar
    search_fields = ['apellido', 'nota']

admin.site.register(Estudiante, Estudianteadmin)

